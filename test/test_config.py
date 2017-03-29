from sendgrid.helpers.inbound.config import Config
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.config = Config()

    def test_initialization(self):
        endpoint = '/inbound'
        port = 5000
        debug_mode = True
        keys = ['from',
                'attachments',
                'headers',
                'text',
                'envelope',
                'to',
                'html',
                'sender_ip',
                'attachment-info',
                'subject',
                'dkim',
                'SPF',
                'charsets',
                'content-ids',
                'spam_report',
                'spam_score',
                'email']
        host = 'http://127.0.0.1:5000/inbound'
        self.assertTrue(debug_mode, self.config.debug_mode)
        self.assertTrue(endpoint, self.config.endpoint)
        self.assertTrue(host, self.config.host)
        self.assertTrue(port, self.config.port)
        for key in keys:
            self.assertTrue(key in self.config.keys)
