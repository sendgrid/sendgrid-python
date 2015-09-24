from .base_test import BaseTest, MockSendGridAPIClientRequest
import os
try:
    import unittest2 as unittest
except ImportError:
    import unittest
try:
    from StringIO import StringIO
except ImportError:  # Python 3
    from io import StringIO

import sendgrid
from sendgrid.client import SendGridAPIClient
from sendgrid.version import __version__

SG_KEY  = os.getenv('SG_KEY') or 'SENDGRID_APIKEY'

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
        self.assertEqual(status, 201)
        self.assertEqual(msg['name'], name)
        
    def test_apikeys_patch(self):
        name = "My NEW Amazing API Key of Wonder [PATCH TEST]"
        status, msg = self.client.apikeys.patch(SG_KEY, name)
        self.assertEqual(status, 200)
        self.assertEqual(msg['name'], name)
        
    def test_apikeys_delete(self):
        status, msg = self.client.apikeys.delete(SG_KEY)
        self.assertEqual(status, 204)

    def test_apikeys_get(self):
        status, msg = self.client.apikeys.get()
        self.assertEqual(status, 200)

if __name__ == '__main__':
    unittest.main()