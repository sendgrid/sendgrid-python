import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# List all bounces #
# GET /suppression/bounces #

params = {'start_time': 0, 'end_time': 0}
response = sg.client.suppression.bounces.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete bounces #
# DELETE /suppression/bounces #

response = sg.client.suppression.bounces.delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get a Bounce #
# GET /suppression/bounces/{email} #

email = "test_url_param"
response = sg.client.suppression.bounces._(email).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a bounce #
# DELETE /suppression/bounces/{email} #

params = {'email_address': 'test_string'}
email = "test_url_param"
response = sg.client.suppression.bounces._(email).delete(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

