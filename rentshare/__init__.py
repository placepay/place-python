"""
RentShare python library
------------------------

Documentation: https://developer.rentshare.com

:copyright: (c) 2017 RentShare (http://rentshare.com)
:license: MIT License
"""

from .__about__ import __version__

PROD_URL = 'https://api.rentshare.com'
TEST_URL = 'https://staging-api.rentshare.com'

api_key = None
api_url = PROD_URL

from rentshare.client import Client
default_client = Client()

from rentshare.exceptions import *
from rentshare.resources import *
