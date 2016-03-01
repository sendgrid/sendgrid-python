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
# List all API Keys belonging to the authenticated user #
# GET /api_keys #

response = self.sg.client.api_keys.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update the name & scopes of an API Key #
# PUT /api_keys/{api_key_id} #

data = {'sample': 'data'}
api_key_id = "test_url_param"
response = self.sg.client.api_keys._(api_key_id).put(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update API keys #
# PATCH /api_keys/{api_key_id} #

data = {'sample': 'data'}
api_key_id = "test_url_param"
response = self.sg.client.api_keys._(api_key_id).patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get an existing API Key #
# GET /api_keys/{api_key_id} #

api_key_id = "test_url_param"
response = self.sg.client.api_keys._(api_key_id).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete API keys #
# DELETE /api_keys/{api_key_id} #

api_key_id = "test_url_param"
response = self.sg.client.api_keys._(api_key_id).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

