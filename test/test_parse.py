from sendgrid.helpers.inbound.config import Config
from sendgrid.helpers.inbound.app import app

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.config = Config()
        self.tester = app.test_client(self)

    def test_parse(self):
        response = self.tester.post(self.config.endpoint,
                                    data='{"Message:", "Success"}')
        self.assertEqual(response.status_code, 200)
