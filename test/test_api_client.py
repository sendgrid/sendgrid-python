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

if __name__ == '__main__':
    unittest.main()