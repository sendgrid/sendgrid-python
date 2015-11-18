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

class TestStats(unittest.TestCase):
    def setUp(self):
        SendGridAPIClient = MockSendGridAPIClientRequest
        self.client = SendGridAPIClient(SG_KEY)
        
    def test_stats_init(self):
        self.stats = self.client.stats
        self.assertEqual(self.stats.base_endpoint, "/v3/stats?")
        self.assertEqual(self.stats.endpoint, "/v3/stats?")
        self.assertEqual(self.stats.client, self.client)

    def test_stats_get(self):
        status, msg = self.client.stats.get('2015-01-01')
        self.assertEqual(status, 200)
        status, msg = self.client.stats.get('2015-01-01', '2015-01-02')
        self.assertEqual(status, 200)
        status, msg = self.client.stats.get('2015-01-01', '2015-01-02', 'day')
        self.assertEqual(status, 200)
        status, msg = self.client.stats.get('2015-01-01', None, 'week')
        self.assertEqual(status, 200)
        status, msg = self.client.stats.get('2015-01-01', None, 'month')
        self.assertEqual(status, 200)

if __name__ == '__main__':
    unittest.main()