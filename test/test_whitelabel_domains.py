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

class TestWhitelabelDomains(unittest.TestCase):
    def setUp(self):
        SendGridAPIClient = MockSendGridAPIClientRequest
        self.client = SendGridAPIClient(SG_KEY)

    def test_whitelabel_domains_init(self):
        self.whitelabel_domains = self.client.whitelabel_domains
        self.assertEqual(self.whitelabel_domains.base_endpoint, "/v3/whitelabel/domains")
        self.assertEqual(self.whitelabel_domains.endpoint, "/v3/whitelabel/domains")
        self.assertEqual(self.whitelabel_domains.client, self.client)

    def test_whitelabel_domains_post(self):
        domain = "nextdoor-test-whitelabel.com"
        subdomain = "test"
        username = "test-subuser1"
        default = True
        status, msg = self.client.whitelabel_domains.post(domain, subdomain, username, default)
        self.assertEqual(status, 201)
        self.assertEqual(msg['domain'], domain)
        self.assertEqual(msg['subdomain'], subdomain)
        self.assertEqual(msg['username'], username)
        self.assertEqual(msg['default'], default)

    def test_whitelabel_domains_patch(self):
        id = 1
        default = False
        status, msg = self.client.whitelabel_domains.patch(id, default)
        self.assertEqual(status, 200)

        self.test_whitelabel_domains_get()

    def test_whitelabel_domains_delete(self):
        id = 1
        status, msg = self.client.whitelabel_domains.delete(id)
        self.assertEqual(status, 204)

        self.test_whitelabel_domains_get()

    def test_whitelabel_domains_get(self):
        status, msg = self.client.whitelabel_domains.get()
        self.assertEqual(self.client.whitelabel_domains.endpoint, "/v3/whitelabel/domains")
        self.assertEqual(status, 200)

if __name__ == '__main__':
    unittest.main()
