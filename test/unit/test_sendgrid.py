import socket
import unittest
from unittest.mock import patch
import urllib.error

import sendgrid
from sendgrid.helpers.mail.exceptions import SendGridTimeoutError

class UnitTests(unittest.TestCase):
    def test_host_with_no_region(self):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY')
        self.assertEqual("https://api.sendgrid.com",sg.client.host)

    def test_host_with_eu_region(self):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY')
        sg.set_sendgrid_data_residency("eu")
        self.assertEqual("https://api.eu.sendgrid.com",sg.client.host)

    def test_host_with_global_region(self):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY')
        sg.set_sendgrid_data_residency("global")
        self.assertEqual("https://api.sendgrid.com",sg.client.host)

    def test_with_region_is_none(self):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY')
        with self.assertRaises(ValueError):
            sg.set_sendgrid_data_residency(None)

    def test_with_region_is_invalid(self):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY')
        with self.assertRaises(ValueError):
            sg.set_sendgrid_data_residency("abc")

    def test_timeout_default(self):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY')
        self.assertEqual(sg.timeout, 30)
        self.assertEqual(sg.client.timeout, 30)

    def test_timeout_set_via_constructor(self):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY', timeout=10)
        self.assertEqual(sg.timeout, 10)
        self.assertEqual(sg.client.timeout, 10)

    @patch('python_http_client.Client')
    def test_send_timeout_raises_sendgrid_timeout_error(self, MockClient):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY')
        sg.client.mail.send.post.side_effect = urllib.error.URLError(
            reason=socket.timeout('timed out'))
        with self.assertRaises(SendGridTimeoutError):
            sg.send({'key': 'value'})