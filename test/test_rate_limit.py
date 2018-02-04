import sendgrid
import os
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class UnitTests(unittest.TestCase):

    def test_rate_limit(self):
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        request_obj = sg.client.access_settings.activity
        response = sg.attempt(request_obj)
        print(response.headers)
        print(response.body)