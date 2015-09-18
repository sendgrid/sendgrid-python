import os
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import json
import sys
try:
    from StringIO import StringIO
except ImportError:  # Python 3
    from io import StringIO
try:
    import urllib.request as urllib_request
    from urllib.parse import urlencode
    from urllib.error import HTTPError
except ImportError:  # Python 2
    import urllib2 as urllib_request
    from urllib2 import HTTPError
    from urllib import urlencode

import sendgrid
from sendgrid import SendGridClient, Mail
from sendgrid.exceptions import SendGridClientError, SendGridServerError
from sendgrid.sendgrid import HTTPError
from sendgrid.client import SendGridAPIClient
from sendgrid.version import __version__

SG_KEY  = os.getenv('SG_KEY') or 'SENDGRID_APIKEY'

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
        print "url= " + req._Request__original
        print "headers= " + str(req.headers)
        print "data= " + json.dumps(data)
        response = 200
        body = {"mock": "success"}
        return response, body

class TestSendGridAPIClient(unittest.TestCase):
    def setUp(self):
        self.client = MockSendGridAPIClientRequest
        self.client = SendGridAPIClient(SG_KEY)

    def test_apikey_init(self):
        self.assertEqual(self.client.apikey, SG_KEY)

    def test_useragent(self):
        useragent = 'sendgrid/' + __version__ + ';python_v3'
        self.assertEqual(self.client.useragent, useragent)

    def test_host(self):
        host = 'https://api.sendgrid.com'
        self.assertEqual(self.client.host, host)

class TestAPIKeys(unittest.TestCase):
    def setUp(self):
        SendGridAPIClient = MockSendGridAPIClientRequest
        self.client = SendGridAPIClient(SG_KEY)
        
    def test_apikeys_init(self):
        self.apikeys = self.client.apikeys
        self.assertEqual(self.apikeys.name, None)
        self.assertEqual(self.apikeys.base_endpoint, "/v3/api_keys")
        self.assertEqual(self.apikeys.endpoint, "/v3/api_keys")
        self.assertEqual(self.apikeys.client, self.client)
        
    def test_apikeys_post(self):
        name = "My Amazing API Key of Wonder [PATCH Test]"
        status, msg = self.client.apikeys.post(name)
        # self.assertEqual(status, 201)
        # msg = json.loads(msg)
        # api_key_id = msg['api_key_id']
        # self.assertEqual(msg['name'], name)
        # print status
        # print msg        

"""
    def test_apikey_post_patch_delete_test(self):
        name = "My Amazing API Key of Wonder [PATCH Test]"
        status, msg = self.client.apikeys.post(name)
        self.assertEqual(status, 201)
        msg = json.loads(msg)
        api_key_id = msg['api_key_id']
        self.assertEqual(msg['name'], name)
        print status
        print msg

        name = "My NEW Amazing API Key of Wonder [PATCH TEST]"
        status, msg = self.client.apikeys.patch(api_key_id, name)
        self.assertEqual(status, 200)
        print status
        print msg

        status, msg = self.client.apikeys.get()
        print status
        print msg

        status, msg = self.client.apikeys.delete(api_key_id)
        self.assertEqual(status, 204)
        print status

        status, msg = self.client.apikeys.get()
        print status
        print msg

    def test_apikey_get(self):
        status, msg = self.client.apikeys.get()
        self.assertEqual(status, 200)
"""

if __name__ == '__main__':
    unittest.main()