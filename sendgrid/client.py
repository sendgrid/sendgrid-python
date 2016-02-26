import python_http_client
import json
import os
from .version import __version__

class SendGridAPIClient(object):

    """SendGrid API."""

    def __init__(self, **opts):
        """
        Construct SendGrid v3 API object.

        Args:
            opts: You can pass in a different host
        """
        path = "/Users/thinkingserious/Workspace/sendgrid-python"
        python_http_client.Config(path)
        self._apikey = os.environ.get('SENDGRID_API_KEY')
        self.useragent = 'sendgrid/' + __version__ + ';python_v3'
        self.host = opts.get('host', 'https://api.sendgrid.com')
        self.path = opts.get('path', os.path.abspath(os.path.dirname(__file__)))
        self.version = __version__

        headers = {
                    "Authorization": "Bearer " + self._apikey,
                    "Content-Type": "application/json",
                    "User-agent": self.useragent
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