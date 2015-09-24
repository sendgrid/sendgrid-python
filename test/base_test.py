import sendgrid
from sendgrid.client import SendGridAPIClient
try:
    import urllib.request as urllib_request
    from urllib.parse import urlencode
    from urllib.error import HTTPError
except ImportError:  # Python 2
    import urllib2 as urllib_request
    from urllib2 import HTTPError
    from urllib import urlencode

class BaseTest():
    def __init__(self):
        pass
        
class MockSendGridAPIClientRequest(SendGridAPIClient):
    def __init__(self, apikey, **opts):
        super(MockSendGridAPIClientRequest, self).__init__(apikey, **opts)
        self._req = None
        
    def _build_request(self, url=None, json_header=False, method='GET', data=None):
        req = urllib_request.Request(url)
        req.get_method = lambda: method
        req.add_header('User-Agent', self.useragent)
        req.add_header('Authorization', 'Bearer ' + self.apikey)
        if json_header:
            req.add_header('Content-Type', 'application/json')
        body = data
        if method == 'POST':
            response = 201
        if method == 'PATCH':
            response = 200
        if method == 'DELETE':
            response = 204
        if method == 'GET':
            response = 200
        return response, body