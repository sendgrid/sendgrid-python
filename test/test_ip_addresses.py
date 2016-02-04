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

class TestIPAddresses(unittest.TestCase):
    def setUp(self):
        SendGridAPIClient = MockSendGridAPIClientRequest
        self.client = SendGridAPIClient(SG_KEY)

    def test_ips_init(self):
        self.ips = self.client.ips
        self.assertEqual(self.ips.base_endpoint, "/v3/ips")
        self.assertEqual(self.ips.endpoint, "/v3/ips")
        self.assertEqual(self.ips.client, self.client)

    def test_ips_post(self):
        ip_pool = 'test-pool'
        ip = '10.1.2.3'
        status, msg = self.client.ips.post(ip_pool, ip)
        self.assertEqual(status, 201)
        self.assertEqual(msg['ip'], ip)

    def test_ips_delete(self):
        ip_pool = 'test-pools'
        ip = '10.1.2.3'
        status, msg = self.client.ips.delete(ip_pool, ip)
        self.assertEqual(status, 204)

        self.test_ips_get()

    def test_ips_get(self):
        status, msg = self.client.ips.get()
        self.assertEqual(self.client.ips.endpoint, "/v3/ips")
        self.assertEqual(status, 200)

if __name__ == '__main__':
    unittest.main()
