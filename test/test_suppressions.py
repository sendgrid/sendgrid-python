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

class TestSuppressions(unittest.TestCase):
    def setUp(self):
        SendGridAPIClient = MockSendGridAPIClientRequest
        self.client = SendGridAPIClient(SG_KEY)
        
    def test_suppressions_init(self):
        self.suppressions = self.client.suppressions
        self.assertEqual(self.suppressions.base_endpoint, "/v3/suppression/unsubscribes")
        self.assertEqual(self.suppressions.endpoint, "/v3/suppression/unsubscribes")
        self.assertEqual(self.suppressions.client, self.client)

    def test_suppressions_get(self):
        status, msg = self.client.suppressions.get()
        self.assertEqual(status, 200)

if __name__ == '__main__':
    unittest.main()