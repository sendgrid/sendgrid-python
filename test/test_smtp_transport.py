import unittest, fudge
import sendgrid
from sendgrid.transport import smtp


class TestTransports(unittest.TestCase):
    def setUp(self):
        self.smtp_connect = fudge.patch_object("smtplib.SMTP", "connect", fudge.Fake('smtp.connect')\
            .expects_call().returns((220, "OK")))


    def tearDown(self):
        self.smtp_connect.restore()


    def test_smtp_transport_wrong_password(self):
        fake_login = fudge.Fake('smtp.login')
        smtp_login = fudge.patch_object("smtplib.SMTP", "login", fake_login)
        fake_login.expects_call().with_args('username', 'password').raises(Exception("SMTP authentication error"))

        message = sendgrid.Message("example@example.com", "subject1", "plain_text", "html")
        smtp_transport = smtp.Smtp('username', 'password', tls=False)
        self.assertRaises(sendgrid.exceptions.SGServiceException, smtp_transport.send, message)

        smtp_login.restore()


    def test_smtp_transport_valid_password(self):
        smtp_login = fudge.patch_object("smtplib.SMTP", "login", fudge.Fake('smtp.login')\
            .expects_call().with_args('username', 'password'))
        smtp_sendmail = fudge.patch_object("smtplib.SMTP", "sendmail", fudge.Fake('smtp.sendmail')\
            .expects_call())
        smtp_quit = fudge.patch_object("smtplib.SMTP", "quit", fudge.Fake('smtp.quit')\
            .expects_call())

        message = sendgrid.Message("example@example.com", "subject1", "plain_text", "html")
        message.add_to("recipient@example.com", "John Doe")
        smtp_transport = smtp.Smtp('username', 'password', tls=False)
        self.assertTrue(smtp_transport.send(message))

        smtp_login.restore()
        smtp_sendmail.restore()
        smtp_quit.restore()


    def test_smtp_transport_content_id_header(self):
        smtp_transport = smtp.Smtp('username', 'password', tls=False)

        f = smtp_transport._getFileMIME({'file': 'img.png', 'name': 'contents'})
        self.assertEqual(None, f.get('Content-ID'))
        self.assertEqual('attachment; filename="contents"', f.get('Content-Disposition'))

        f = smtp_transport._getFileMIME({'file': 'img.png', 'name': 'contents', 'cid': None})
        self.assertEqual(None, f.get('Content-ID'))
        self.assertEqual('attachment; filename="contents"', f.get('Content-Disposition'))

        f = smtp_transport._getFileMIME({'file': 'img.png', 'name': 'contents', 'cid': 'cid'})
        self.assertEqual('<cid>', f.get('Content-ID'))
        self.assertEqual(None, f.get('Content-Disposition'))


class FakeException(IOError):
    def __init__(self, msg):
        self.msg = msg
        super(FakeException, self).__init__()


    def read(self):
        return self.msg


if __name__ == '__main__':
    unittest.main()