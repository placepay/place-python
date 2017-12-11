from rentshare.exceptions import *
import rentshare
import requests
import json
import urlparse
import os
import pprint

def _walk_object( obj, client=None, inverse=False ):
	if isinstance( obj, list ):
		_iter = enumerate( obj )
	else:
		_iter = obj.items()
	for key, val in _iter:
		if inverse:
			if isinstance( val, APIResource ):
				val = obj[key] = val._obj
		elif isinstance( val, dict )\
		and 'object' in val:
			for resource in APIResource.__subclasses__():
				if val['object'] != resource.object_type:
					continue
				val = obj[key] = resource( client=client, **val )
				break
		if isinstance( val, ( list, dict ) ):
			_walk_object( val, client=client )

class APIResource(object):
	resource = None
	object_type = None
	_object_index = {}

	def __new__( cls, client=None, **obj ):
		if 'id' in obj:
			key = '{}_{}'.format( cls.object_type, obj['id'] )
			if key in cls._object_index:
				cls._object_index[key]._set_obj( obj )
				return cls._object_index[key]
		return super( APIResource, cls ).__new__( cls, client=None, **obj )

	def __init__( self, client=None, **obj ):
		self._client = client or rentshare.default_client
		self._set_obj( obj )

	def __repr__(self):
		return '{} (id={})'.format(
			super( APIResource, self ).__repr__(), self.id )

	def _set_obj( self, obj ):
		self._obj = obj
		_walk_object( self._obj, client=self._client )
		if 'id' in obj:
			key = '{}_{}'.format( obj['object'], obj['id'] )
			self._object_index[key] = self

	def __getattr__( self, attr ):
		if attr in self._obj:
			return self._obj[attr]
		return super( APIResource, self ).__getattr__( self, attr )

	@classmethod
	def _request( cls, method, path=None, id=None, client=None, *args, **kwargs):
		path = path or cls.resource
		client = client or rentshare.default_client
		if id:
			path = os.path.join( path, id )
		url = urlparse.urljoin( client.api_url, path.strip('/') )

		kwargs['headers'] = kwargs.get('headers',{})

		kwargs['auth'] = ( client.api_key, '' )

		response = getattr( requests, method )( url, *args, **kwargs )
		status_code = response.status_code

		try:
			obj = response.json()
		except ValueError:
			if status_code == 500:
				raise InternalError()
			raise InvalidResponse()

		if not isinstance( obj, dict ):
			raise InvalidResponse()

		object_type = obj.get('object')
		if not object_type:
			raise InvalidResponse('Response missing "object" attribute')

		if status_code != 200:
			if object_type != 'error':
				raise InvalidResponse('Expected error object')
			for exc in APIException.__subclasses__():
				if exc.status_code != status_code:
					continue
				if exc.error_type and exc.error_type != obj.get('error_type'):
					continue
				raise exc( obj.get('error_description') )
			raise APIException( obj.get('error_description') )

		if object_type == 'list':
			return [ cls( client=client, **o ) for o in obj['values'] ]
		return cls( client=client, **obj )

	def update( self, **updates ):
		self._request( 'put', id=self.id, json=updates )

	def delete( self, **updates ):
		self._request( 'delete', id=self.id )

	@classmethod
	def get( cls, id ):
		return cls._request( 'get', id=id )

	@classmethod
	def select( cls, **filter_by ):
		return cls._request( 'get', params=filter_by )

	@classmethod
	def create( cls, **values ):
		_walk_object( values, inverse=True )
		return cls._request( 'post', json=values )

	@classmethod
	def create_all( cls, objects ):
		return cls._request( 'post',
			json={ "object": "list", "values": objects } )

	@classmethod
	def update_all( cls, objects, **updates ):
		updates = [ dict(id=o.id, **updates) for o in objects ]
		return cls._request( 'put',
			json={ "object": "list", "values": updates } )

	@classmethod
	def delete_all( cls, objects ):
		deletes = '|'.join( map( str, [ o.id for o in objects ] ) )
		return cls._request( 'delete', params={ 'id': deletes } )
