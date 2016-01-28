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

class TestWhitelabelIPs(unittest.TestCase):
    def setUp(self):
        SendGridAPIClient = MockSendGridAPIClientRequest
        self.client = SendGridAPIClient(SG_KEY)

    def test_whitelabel_ips_init(self):
        self.whitelabel_ips = self.client.whitelabel_ips
        self.assertEqual(self.whitelabel_ips.base_endpoint, "/v3/whitelabel/ips")
        self.assertEqual(self.whitelabel_ips.endpoint, "/v3/whitelabel/ips")
        self.assertEqual(self.whitelabel_ips.client, self.client)

    def test_whitelabel_ips_post(self):
        domain = "nextdoor-test-whitelabel.com"
        subdomain = "test"
        ip = '10.1.2.3'
        status, msg = self.client.whitelabel_ips.post(ip, domain, subdomain)
        self.assertEqual(status, 201)
        self.assertEqual(msg['ip'], ip)
        self.assertEqual(msg['domain'], domain)
        self.assertEqual(msg['subdomain'], subdomain)

    def test_whitelabel_ips_delete(self):
        id = 1
        status, msg = self.client.whitelabel_ips.delete(id)
        self.assertEqual(status, 204)

        self.test_whitelabel_ips_get()

    def test_whitelabel_ips_get(self):
        status, msg = self.client.whitelabel_ips.get()
        self.assertEqual(self.client.whitelabel_ips.endpoint, "/v3/whitelabel/ips")
        self.assertEqual(status, 200)

if __name__ == '__main__':
    unittest.main()
