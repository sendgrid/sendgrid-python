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
# Create API keys #
# POST /api_key #

data = {'sample': 'data'}
response = self.sg.client.api_key.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

