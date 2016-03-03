import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# Create a batch ID #
# POST /mail/batch #

data = {'sample': 'data'}
response = sg.client.mail.batch.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Validate batch ID #
# GET /mail/batch/{batch_id} #

batch_id = "test_url_param"
response = sg.client.mail.batch._(batch_id).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

