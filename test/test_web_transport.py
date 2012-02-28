import unittest, fudge
import sendgrid
from sendgrid.transport import web


class TestTransports(unittest.TestCase):
    def test_web_transport_wrong_password(self):
        fake_urlopen = fudge.Fake('urlopen')
        fake_response = fudge.Fake('fake_response')
        urllib = fudge.patch_object("urllib2", "urlopen", fake_urlopen)
        fake_urlopen.expects_call().returns(fake_response)
        fake_response.expects("read").raises(FakeException('{"message": "error", "errors": "Bad username / password"}'))

        message = sendgrid.Message("example@example.com", "subject1", "plain_text", "html")
        message.add_to("recipient@example.com")

        web_transport = web.Http('username', 'password')
        self.assertRaises(sendgrid.exceptions.SGServiceException, web_transport.send, message)

        urllib.restore()


    def test_web_transport_valid_password(self):
        fake_urlopen = fudge.Fake('urlopen')
        fake_response = fudge.Fake('fake_response')
        fake_urlencode = fudge.Fake('urlencode')

        urllib2 = fudge.patch_object("urllib2", "urlopen", fake_urlopen)
        fake_urlopen.expects_call().returns(fake_response)
        fake_response.expects("read").returns('{"message": "success", "status": "ok"}')

        message = sendgrid.Message("example@example.com", "subject1", "plain_text", "html")
        message.add_to("recipient@example.com")

        urllib = fudge.patch_object("urllib", "urlencode", fake_urlencode)
        fake_urlencode.expects_call().with_args({'from': 'example@example.com', 'api_user': 'username', 'text': 'plain_text',
                                                 'to': ['recipient@example.com'], 'html': 'html', 'date': message.date,
                                                 'api_key': 'password', 'subject': 'subject1'}, 1).returns("")

        web_transport = web.Http('username', 'password')
        self.assertTrue(web_transport.send(message))

        urllib.restore()
        urllib2.restore()


class FakeException(IOError):
    def __init__(self, msg):
        self.msg = msg
        super(FakeException, self).__init__()


    def read(self):
        return self.msg


if __name__ == '__main__':
    unittest.main()