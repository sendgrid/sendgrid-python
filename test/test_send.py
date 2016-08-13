try:
    import unittest2 as unittest
except ImportError:
    import unittest


class UnitTests(unittest.TestCase):

    def test_send_stub(self):
        self.assertEqual(True, True)