import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

##################################################
# Returns a list of all partner settings. #
# GET /partner_settings #

params = {'limit': 1, 'offset': 1}
response = sg.client.partner_settings.get(query_params=params)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Updates New Relic partner settings. #
# PATCH /partner_settings/new_relic #

data = {
    "enable_subuser_statistics": True,
    "enabled": True,
    "license_key": ""
}
response = sg.client.partner_settings.new_relic.patch(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Returns all New Relic partner settings. #
# GET /partner_settings/new_relic #

response = sg.client.partner_settings.new_relic.get()
print(response.status_code)
print(response.body)
print(response.headers)
