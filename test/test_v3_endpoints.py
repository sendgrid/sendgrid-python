import sendgrid
import json
from sendgrid.client import SendGridAPIClient
from sendgrid.version import __version__
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import os
if os.path.exists('.env'):
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

class TestSendGridAPIClient(unittest.TestCase):
    def setUp(self):
        self.sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
        self.client = sendgrid.SendGridAPIClient(self.sendgrid_api_key)

    def test_apikey_init(self):
        self.assertEqual(self.client.apikey, self.sendgrid_api_key)

    def test_useragent(self):
        useragent = 'sendgrid/' + __version__ + ';python_v3'
        self.assertEqual(self.client.useragent, useragent)

    def test_host(self):
        host = 'https://api.sendgrid.com/v3/'
        self.assertEqual(self.client.host, host)

class TestTemplates(unittest.TestCase):
    template_id = "13b8f94f-bcae-4ec6-b752-70d6cb59f932" #TODO: Configuration
    def setUp(self):
        self.sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
        self.sg = sendgrid.SendGridAPIClient(self.sendgrid_api_key)
        self.templates = self.sg.client.templates
        
    def test_01_templates_get(self):
        response = self.templates.get()
        self.assertEqual(response.status_code, 200)
    
    def test_02_templates_get_specific(self):
        response = self.templates._(self.__class__.template_id).get()
        self.assertEqual(response.status_code, 200)       
    
    def test_03_templates_post(self):
        data = {"name": "Python Client Template Endpoint Test v06"}
        response = self.templates.post(data=data)
        response_json = response.json()
        self.__class__.template_id = response_json['id']
        self.assertEqual(response.status_code, 201)  
        
    def test_04_templates_patch(self):
        data = {"name": "Python Client Template Endpoint Test v07"}
        response = self.templates._(self.__class__.template_id).patch(data=data)
        self.assertEqual(response.status_code, 200)
        
    def test_05_templates_delete(self):
        response = self.templates._(self.__class__.template_id).delete()
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()