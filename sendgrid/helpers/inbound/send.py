"""A module for sending test SendGrid Inbound Parse messages
Usage: ./send.py [path to file containing test data]"""
import os
import sys
from config import Config
from python_http_client import Client

class Send(object):
    def __init__(self, url):
        self._url = url

    def test_payload(self, payload_filepath):
        headers = {
            "User-Agent": "SendGrid-Test",
            "Content-Type": "multipart/form-data; boundary=xYzZY"
        }
        client = Client(host=self.url, request_headers=headers)
        f = open(payload_filepath, 'r')
        data = f.read()
        return client.post(request_body=data)

    @property
    def url(self):
        return self._url

config = Config()
send = Send(config.host)
response = send.test_payload(sys.argv[1])
print response.status_code
print response.headers
print response.body