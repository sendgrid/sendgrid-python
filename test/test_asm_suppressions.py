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
        
    def test_asm_suppressions_init(self):
        self.asm_suppressions = self.client.asm_suppressions
        self.assertEqual(self.asm_suppressions.base_endpoint, "/v3/asm/groups")
        self.assertEqual(self.asm_suppressions.endpoint, "/v3/asm/groups")
        self.assertEqual(self.asm_suppressions.client, self.client)

    def test_asm_suppressions_get(self):
        status, msg = self.client.asm_suppressions.get(70)
        self.assertEqual(status, 200)
        
    def test_asm_suppressions_post(self):
        id = 67
        emails = ['elmer+test@thinkingserious.com']
        status, msg = self.client.asm_suppressions.post(id, emails)
        self.assertEqual(status, 201)
        self.assertEqual(msg['recipient_emails'], emails)
        emails = ['elmer+test@thinkingserious.com', 'elmer.thomas@yahoo.com']
        status, msg = self.client.asm_suppressions.post(id, emails)
        self.assertEqual(status, 201)
        self.assertEqual(msg['recipient_emails'], emails)
        
    def test_asm_supressions_delete(self):
        id = 67
        email = 'elmer+test@thinkingserious.com'
        status, msg = self.client.asm_suppressions.delete(id, email)
        self.assertEqual(status, 204)

if __name__ == '__main__':
    unittest.main()