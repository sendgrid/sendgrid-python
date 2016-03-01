import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient()

response = sg.client.asm.suppressions._("global").get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)