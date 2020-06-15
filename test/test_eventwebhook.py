import json
import unittest

from sendgrid import EventWebhook


class UnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.PUBLIC_KEY = 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEEDr2LjtURuePQzplybdC+u4CwrqDqBaWjcMMsTbhdbcwHBcepxo7yAQGhHPTnlvFYPAZFceEu/1FwCM/QmGUhA=='
        cls.SIGNATURE = 'MEUCIQCtIHJeH93Y+qpYeWrySphQgpNGNr/U+UyUlBkU6n7RAwIgJTz2C+8a8xonZGi6BpSzoQsbVRamr2nlxFDWYNH2j/0='
        cls.TIMESTAMP = '1588788367'
        cls.PAYLOAD = json.dumps({
            'event': 'test_event',
            'category': 'example_payload',
            'message_id': 'message_id',
        }, sort_keys=True, separators=(',', ':'))

    def test_verify_valid_signature(self):
        ew = EventWebhook()
        key = ew.convert_public_key_to_ecdsa(self.PUBLIC_KEY)
        self.assertTrue(ew.verify_signature(self.PAYLOAD, self.SIGNATURE, self.TIMESTAMP, key))

    def test_verify_bad_key(self):
        ew = EventWebhook('MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEqTxd43gyp8IOEto2LdIfjRQrIbsd4SXZkLW6jDutdhXSJCWHw8REntlo7aNDthvj+y7GjUuFDb/R1NGe1OPzpA==')
        self.assertFalse(ew.verify_signature(self.PAYLOAD, self.SIGNATURE, self.TIMESTAMP))

    def test_verify_bad_payload(self):
        ew = EventWebhook(self.PUBLIC_KEY)
        self.assertFalse(ew.verify_signature('payload', self.SIGNATURE, self.TIMESTAMP))

    def test_verify_bad_signature(self):
        ew = EventWebhook(self.PUBLIC_KEY)
        self.assertFalse(ew.verify_signature(
            self.PAYLOAD,
            'MEUCIQCtIHJeH93Y+qpYeWrySphQgpNGNr/U+UyUlBkU6n7RAwIgJTz2C+8a8xonZGi6BpSzoQsbVRamr2nlxFDWYNH3j/0=',
            self.TIMESTAMP
        ))

    def test_verify_bad_timestamp(self):
        ew = EventWebhook(self.PUBLIC_KEY)
        self.assertFalse(ew.verify_signature(self.PAYLOAD, self.SIGNATURE, 'timestamp'))
