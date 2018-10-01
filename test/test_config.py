import os
import unittest

import sendgrid.helpers.inbound.config
from sendgrid.helpers.inbound.config import Config


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
            self.assertIn(key, self.config.keys)

    def test_init_environment(self):
        config_file = sendgrid.helpers.inbound.config.__file__
        env_file_path = os.path.abspath(os.path.dirname(config_file)) + '/.env'
        with open(env_file_path, 'w') as f:
            f.write('RANDOM_VARIABLE=RANDOM_VALUE')
        Config()
        os.remove(env_file_path)
        self.assertEqual('RANDOM_VALUE', os.environ['RANDOM_VARIABLE'])
