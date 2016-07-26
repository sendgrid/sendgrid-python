import os
import python_http_client

from .version import __version__

class SendGridAPIClient(object):
    """SendGrid API."""
    def __init__(self, **opts):
        """
        Construct SendGrid v3 API object.

        :params host: Base URL for the API call
        :type host: string
        """
        self.path = opts.get('path', os.path.abspath(os.path.dirname(__file__)))
        self._apikey = opts.get('apikey', os.environ.get('SENDGRID_API_KEY'))
        # Support v2 api_key naming
        self._apikey = opts.get('api_key', self._apikey)
        self._api_key = self._apikey
        self.useragent = 'sendgrid/{0};python'.format(__version__)
        self.host = opts.get('host', 'https://api.sendgrid.com')
        self.version = __version__

        headers = {
            "Authorization": 'Bearer {0}'.format(self._apikey),
            "User-agent": self.useragent,
            "Accept": 'application/json'
        }

        self.client = python_http_client.Client(host=self.host,
                                                request_headers=headers,
                                                version=3)

    @property
    def apikey(self):
        return self._apikey

    @apikey.setter
    def apikey(self, value):
        self._apikey = value

    @property
    def api_key(self):
        return self._apikey

    @api_key.setter
    def api_key(self, value):
        self._apikey = value