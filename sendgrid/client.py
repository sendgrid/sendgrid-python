from universalclient import Client, jsonFilter
import json
from .version import __version__
class SendGridAPIClient(object):

    """SendGrid API."""

    def __init__(self, apikey, **opts):
        """
        Construct SendGrid v3 API object.

        Args:
            apikey: SendGrid API key
            opts: You can pass in a different host
        """
        self._apikey = apikey
        self.useragent = 'sendgrid/' + __version__ + ';python_v3'
        self.host = opts.get('host', 'https://api.sendgrid.com/v3/')
        self.version = __version__

        headers = "{\"Authorization\": \"Bearer " + self._apikey + "\", \
                    \"Content-Type\": \"application/json\", \
                    \"User-agent\": \"" + self.useragent + "\"}"
                    
        self.client = Client(self.host, dataFilter=jsonFilter, headers=json.loads(headers))

    @property
    def apikey(self):
        return self._apikey

    @apikey.setter
    def apikey(self, value):
        self._apikey = value