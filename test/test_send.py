try:
    import unittest2 as unittest
except ImportError:
    import unittest

try:
    import unittest.mock as mock
except ImportError:
    import mock


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.client_mock = mock.patch('sendgrid.helpers.inbound.send.Client')
        self.open_mock = mock.patch('sendgrid.helpers.inbound.send.open',
                                    mock.mock_open(), create=True)
        self.client_mock.start()
        self.open_mock.start()

    def tearDown(self):
        self.client_mock.stop()
        self.open_mock.stop()

    def test_send(self):
        from sendgrid.helpers.inbound import send

        fake_url = 'https://fake_url'
        x = send.Send(fake_url)
        x.test_payload(fake_url)

        send.Client.assert_called_once_with(host=fake_url, request_headers={'User-Agent': 'SendGrid-Test',
                                                                       'Content-Type': 'multipart/form-data; boundary=xYzZY'})
