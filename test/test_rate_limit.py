import sendgrid
import os
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class UnitTests(unittest.TestCase):

    def test_rate_limit(self):
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        query_params = {}
        data = {}
        request_obj = sg.client.access_settings.activity
        response = sg.make_request(request_obj,
                              query_params=query_params,
                              method="get",
                              request_body=data)
        print(response.status_code)
        print(response.headers)
        print(response.body)