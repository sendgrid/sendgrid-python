import unittest
import sendgrid

class UnitTests(unittest.TestCase):
    def test_host_with_no_region(self):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY')
        self.assertEqual("https://api.sendgrid.com",sg.client.host)

    def test_host_with_eu_region(self):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY')
        sg.set_data_residency("eu")
        self.assertEqual("https://api.eu.sendgrid.com",sg.client.host)

    def test_host_with_global_region(self):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY')
        sg.set_data_residency("global")
        self.assertEqual("https://api.sendgrid.com",sg.client.host)

    def test_host_with_host_first_eu_region_second(self):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY')
        sg.set_host("https://sendgrid.com")
        sg.set_data_residency("eu")
        self.assertEqual("https://api.eu.sendgrid.com",sg.client.host)

    def test_host_with_eu_first_host_second(self):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY')
        sg.set_data_residency("eu")
        sg.set_host("https://sendgrid.com")
        self.assertEqual("https://sendgrid.com",sg.client.host)

    def test_host_using_constructor(self):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY',host='https://sendgrid.com')
        self.assertEqual("https://sendgrid.com",sg.client.host)

    def test_with_region_is_none(self):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY')
        with self.assertRaises(ValueError):
            sg.set_data_residency(None)

    def test_with_region_is_invalid(self):
        sg = sendgrid.SendGridAPIClient(api_key='MY_API_KEY')
        with self.assertRaises(ValueError):
            sg.set_data_residency("abc")