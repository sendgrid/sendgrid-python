import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient()

##################################################
# Create API keys #
# POST /api_key #

data = {'sample': 'data'}
response = sg.client.api_key.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

