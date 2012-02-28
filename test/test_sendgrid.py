import unittest
import sendgrid
from sendgrid.transport import web, smtp


class TestSendgrid(unittest.TestCase):
    def test_object_creation(self):
        s = sendgrid.Sendgrid('username1', 'my_secret')
        self.assertTrue(isinstance(s.web, web.Http))
        self.assertTrue(isinstance(s.smtp, smtp.Smtp))


if __name__ == '__main__':
    unittest.main()