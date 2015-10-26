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

class TestASMGroups(unittest.TestCase):
    def setUp(self):
        SendGridAPIClient = MockSendGridAPIClientRequest
        self.client = SendGridAPIClient(SG_KEY)
        
    def test_asm_global_suppressions_init(self):
        self.asm_global_suppressions = self.client.asm_global_suppressions
        self.assertEqual(self.asm_global_suppressions.base_endpoint, "/v3/asm/suppressions/global")
        self.assertEqual(self.asm_global_suppressions.endpoint, "/v3/asm/suppressions/global")
        self.assertEqual(self.asm_global_suppressions.client, self.client)

    def test_asm_global_suppressions_get(self):
        status, msg = self.client.asm_global_suppressions.get('test@example.com')
        self.assertEqual(status, 200)
        
    def test_asm_global_suppressions_post(self):
        emails = ['elmer+test@thinkingserious.com']
        status, msg = self.client.asm_global_suppressions.post(emails)
        self.assertEqual(status, 201)
        self.assertEqual(msg['recipient_emails'], emails)
        emails = ['elmer+test@thinkingserious.com', 'elmer.thomas@yahoo.com']
        status, msg = self.client.asm_global_suppressions.post(emails)
        self.assertEqual(status, 201)
        self.assertEqual(msg['recipient_emails'], emails)
        
    def test_asm_global_suppressions_delete(self):
        status, msg = self.client.asm_global_suppressions.delete('test@example.com')
        self.assertEqual(status, 204)

if __name__ == '__main__':
    unittest.main()