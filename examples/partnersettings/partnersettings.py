import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# Returns a list of all partner settings. #
# GET /partner_settings #

params = {'limit': 1, 'offset': 1}
response = sg.client.partner_settings.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Returns all New Relic partner settings. #
# GET /partner_settings/new_relic #

response = sg.client.partner_settings.new_relic.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Updates New Relic partner settings. #
# PATCH /partner_settings/new_relic #

data = {
  "enable_subuser_statistics": true, 
  "enabled": true, 
  "license_key": ""
}
response = sg.client.partner_settings.new_relic.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get SendWithUs Settings #
# GET /partner_settings/sendwithus #

response = sg.client.partner_settings.sendwithus.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update SendWithUs Settings #
# PATCH /partner_settings/sendwithus #

response = sg.client.partner_settings.sendwithus.patch()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

