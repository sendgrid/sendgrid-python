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
# Returns a list of all partner settings. #
# GET /partner_settings #

params = {'limit': 0, 'offset': 0}
response = self.sg.client.partner_settings.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Updates New Relic partner settings. #
# PATCH /partner_settings/new_relic #

data = {'sample': 'data'}
response = self.sg.client.partner_settings.new_relic.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Returns all New Relic partner settings. #
# GET /partner_settings/new_relic #

response = self.sg.client.partner_settings.new_relic.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update SendWithUs Settings #
# PATCH /partner_settings/sendwithus #

data = {'sample': 'data'}
response = self.sg.client.partner_settings.sendwithus.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get SendWithUs Settings #
# GET /partner_settings/sendwithus #

response = self.sg.client.partner_settings.sendwithus.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

