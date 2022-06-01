import os, uuid
from time import sleep
from urllib.parse import urlparse
from urllib.parse import parse_qs

# Would be nice to not need azure branded imports.
from azure.core.credentials import AccessToken
from azure.core.exceptions import HttpResponseError

from DigitalOceanClient import DigitalOceanAPI
from digitalocean.models import Droplet

REGION = "nyc3"

class DigitalOceanError(Exception):
    pass

# We should hide the need for this if possible...
class TokenCredentials:
    def __init__(self, api_token):
        self._token = api_token
        self._expires_on = 0

    def get_token(self, *args, **kwargs) -> AccessToken:
        return AccessToken(self._token, expires_on=self._expires_on)