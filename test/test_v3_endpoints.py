import sendgrid
import json
from sendgrid.client import SendGridAPIClient
from sendgrid.version import __version__
from sendgrid.config import Config
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import os
config = Config()

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

class TestAPIKeys(unittest.TestCase):
    api_key_id = ""
    def setUp(self):
        self.sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
        self.sg = sendgrid.SendGridAPIClient(self.sendgrid_api_key)
        self.api_keys = self.sg.client.api_keys
        scopes = self.sg.client.scopes
        response = scopes.get()
        response_json = response.json()
        self.scope = response_json['scopes']

    def test_00_api_keys_post(self):
        data = {"name": "Python Client APIKeys Test v4000"}
        response = self.api_keys.post(data=data)
        self.assertEqual(response.status_code, 201)
        response_json = response.json()
        self.__class__.api_key_id = response_json['api_key_id']

    def test_01_api_keys_get(self):
        response = self.api_keys.get()
        self.assertEqual(response.status_code, 200)
    
    def test_02_api_keys_get_specific(self):
        response = self.api_keys._(self.__class__.api_key_id).get()
        self.assertEqual(response.status_code, 200)       
        
    def test_03_api_keys_patch(self):
        data = {"name": "Python Client APIKeys Test v4001"}
        response = self.api_keys._(self.__class__.api_key_id).patch(data=data)
        self.assertEqual(response.status_code, 200)
        
    def test_04_api_keys_put(self):
        data = {"name": "Python Client Template Endpoint Test v4002", "scopes": self.scope}
        response = self.api_keys._(self.__class__.api_key_id).put(data=data)
        self.assertEqual(response.status_code, 200)
        
    def test_05_api_keys_delete(self):
        response = self.api_keys._(self.__class__.api_key_id).delete()
        self.assertEqual(response.status_code, 204) 

class TestTemplates(unittest.TestCase):
    template_id = ""
    def setUp(self):
        self.sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
        self.sg = sendgrid.SendGridAPIClient(self.sendgrid_api_key)
        self.templates = self.sg.client.templates

    def test_00_templates_post(self):
        data = {"name": "Python Client Template Endpoint Test v4000"}
        response = self.templates.post(data=data)
        response_json = response.json()
        self.__class__.template_id = response_json['id']
        self.assertEqual(response.status_code, 201)

    def test_01_templates_get(self):
        response = self.templates.get()
        self.assertEqual(response.status_code, 200)
    
    def test_02_templates_get_specific(self):
        response = self.templates._(self.__class__.template_id).get()
        self.assertEqual(response.status_code, 200)       
        
    def test_03_templates_patch(self):
        data = {"name": "Python Client Template Endpoint Test v4001"}
        response = self.templates._(self.__class__.template_id).patch(data=data)
        self.assertEqual(response.status_code, 200)
        
    def test_04_templates_delete(self):
        response = self.templates._(self.__class__.template_id).delete()
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()