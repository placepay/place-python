from rentshare.api_resource import APIResource

class AccessToken( APIResource ):
	resource = '/access_tokens'
	object_type = 'access_token'

class AutopayEnrollment( APIResource ):
	resource = '/autopay_enrollments'
	object_type = 'autopay_enrollment'

class Event( APIResource ):
	resource = '/events'
	object_type = 'event'

class Account( APIResource ):
	resource = '/accounts'
	object_type = 'account'

class DepositAccount( APIResource ):
	resource = '/deposit_accounts'
	object_type = 'deposit_account'

class Transaction( APIResource ):
	resource = '/transactions'
	object_type = 'transaction'

class Address( APIResource ):
	resource = '/addresses'
	object_type = 'address'
