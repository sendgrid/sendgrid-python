import sendgrid
import os
sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
host = os.environ.get('HOST') # e.g. https://api.sendgrid.com
request_headers = {
    "Authorization": 'Bearer {0}'.format(sendgrid_api_key),
    "Content-Type": "application/json"
}
sg = sendgrid.SendGridAPIClient(host=host, request_headers=request_headers)

##################################################
# Create a batch ID #
# POST /mail/batch #

data = {'sample': 'data'}
response = self.sg.client.mail.batch.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Validate batch ID #
# GET /mail/batch/{batch_id} #

batch_id = "test_url_param"
response = self.sg.client.mail.batch._(batch_id).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

