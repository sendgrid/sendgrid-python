import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# Create API keys #
# POST /api_key #

data = {'sample': 'data'}
response = sg.client.api_key.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

