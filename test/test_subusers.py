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

class TestSubusers(unittest.TestCase):
    def setUp(self):
        SendGridAPIClient = MockSendGridAPIClientRequest
        self.client = SendGridAPIClient(SG_KEY)

    def test_subusers_init(self):
        self.subusers = self.client.subusers
        self.assertEqual(self.subusers.name, None)
        self.assertEqual(self.subusers.base_endpoint, "/v3/subusers")
        self.assertEqual(self.subusers.endpoint, "/v3/subusers")
        self.assertEqual(self.subusers.client, self.client)

    def test_subusers_post(self):
        username = "test-subuser1"
        email = "keiji+test-subuser1@nextdoor.com"
        password = "password"
        status, msg = self.client.subusers.post(username, email, password)
        self.assertEqual(status, 201)
        self.assertEqual(msg['username'], username)
        self.assertEqual(msg['email'], email)
        self.assertEqual(msg['password'], password)

    def test_subusers_patch(self):
        username = "test-subuser1"
        disabled = True
        status, msg = self.client.subusers.patch(username, disabled)
        self.assertEqual(status, 200)

    def test_subusers_delete(self):
        username = "test-subuser1"
        status, msg = self.client.subusers.delete(username)
        self.assertEqual(status, 204)

    def test_subusers_get(self):
        status, msg = self.client.subusers.get()
        self.assertEqual(status, 200)

if __name__ == '__main__':
    unittest.main()
