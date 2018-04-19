import place
import place.resources
from functools import partial


class Client(object):
    def __init__(self, api_key=None, api_url=None):
        self._api_key = api_key
        self._api_url = api_url

    @property
    def api_key(self):
        return self._api_key or place.api_key

    @property
    def api_url(self):
        return self._api_url or place.api_url
