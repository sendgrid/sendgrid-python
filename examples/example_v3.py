import sendgrid
import json
import os

host = "http://localhost:4010"
path = os.path.abspath(os.path.dirname(__file__)) + "/.."
sg = sendgrid.SendGridAPIClient(host=host, path=path)

data = {"sample": "data", "X-Mock": 204}
response = sg.client.asm.suppressions._("global").post(request_headers=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)