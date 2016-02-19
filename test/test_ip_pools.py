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

class TestIPPools(unittest.TestCase):
    def setUp(self):
        SendGridAPIClient = MockSendGridAPIClientRequest
        self.client = SendGridAPIClient(SG_KEY)

    def test_ip_pools_init(self):
        self.ip_pools = self.client.ip_pools
        self.assertEqual(self.ip_pools.base_endpoint, "/v3/ips/pools")
        self.assertEqual(self.ip_pools.endpoint, "/v3/ips/pools")
        self.assertEqual(self.ip_pools.client, self.client)

    def test_ip_pools_post(self):
        name = 'test-pool'
        status, msg = self.client.ip_pools.post(name)
        self.assertEqual(status, 201)
        self.assertEqual(msg['name'], name)

    def test_ip_pools_delete(self):
        id = 'test-pools'
        status, msg = self.client.ip_pools.delete(id)
        self.assertEqual(status, 204)

        self.test_ip_pools_get()

    def test_ip_pools_get(self):
        status, msg = self.client.ip_pools.get()
        self.assertEqual(self.client.ip_pools.endpoint, "/v3/ips/pools")
        self.assertEqual(status, 200)

if __name__ == '__main__':
    unittest.main()
