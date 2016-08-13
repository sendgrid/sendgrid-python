from sendgrid.helpers.inbound.parse import Parse
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class UnitTests(unittest.TestCase):

    def test_parse_stub(self):
        self.assertEqual(True, True)