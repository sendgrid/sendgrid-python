from sendgrid.helpers.inbound.config import Config
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class UnitTests(unittest.TestCase):

    def test_config_stub(self):
        self.assertEqual(True, True)