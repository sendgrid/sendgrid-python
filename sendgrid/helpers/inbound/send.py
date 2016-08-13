import os
from python_http_client import Client

class Send(object):
    def __init__(self, url):
        self._url = url
        pass

    def test_payload(self, payload_filepath):
        base_url = "http://127.0.0.1:5000/inbound"
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

send = Send('http://127.0.0.1:5000/inbound')
# TODO: should take the path as an argument
dir_path = os.path.dirname(os.path.realpath(__file__))
response = send.test_payload(dir_path + '/sample_data/default_data.txt')
print response.status_code
print response.headers
print response.body