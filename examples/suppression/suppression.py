import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# Retrieve all blocks #
# GET /suppression/blocks #

params = {'start_time': 1, 'limit': 1, 'end_time': 1, 'offset': 1}
response = sg.client.suppression.blocks.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete blocks #
# DELETE /suppression/blocks #

response = sg.client.suppression.blocks.delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a specific block #
# DELETE /suppression/blocks/{email} #

email = "test_url_param"
response = sg.client.suppression.blocks._(email).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve a specific block #
# GET /suppression/blocks/{email} #

email = "test_url_param"
response = sg.client.suppression.blocks._(email).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve all bounces #
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
# Retrieve a Bounce #
# GET /suppression/bounces/{email} #

email = "test_url_param"
response = sg.client.suppression.bounces._(email).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a bounce #
# DELETE /suppression/bounces/{email} #

params = {'email_address': 'example@example.com'}
email = "test_url_param"
response = sg.client.suppression.bounces._(email).delete(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete invalid emails #
# DELETE /suppression/invalid_emails #

response = sg.client.suppression.invalid_emails.delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve all invalid emails #
# GET /suppression/invalid_emails #

params = {'start_time': 1, 'limit': 1, 'end_time': 1, 'offset': 1}
response = sg.client.suppression.invalid_emails.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve a specific invalid email #
# GET /suppression/invalid_emails/{email} #

email = "test_url_param"
response = sg.client.suppression.invalid_emails._(email).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a specific invalid email #
# DELETE /suppression/invalid_emails/{email} #

email = "test_url_param"
response = sg.client.suppression.invalid_emails._(email).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve a specific spam report #
# GET /suppression/spam_report/{email} #

email = "test_url_param"
response = sg.client.suppression.spam_report._(email).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a specific spam report #
# DELETE /suppression/spam_report/{email} #

email = "test_url_param"
response = sg.client.suppression.spam_report._(email).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete spam reports #
# DELETE /suppression/spam_reports #

response = sg.client.suppression.spam_reports.delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve all spam reports #
# GET /suppression/spam_reports #

params = {'start_time': 1, 'limit': 1, 'end_time': 1, 'offset': 1}
response = sg.client.suppression.spam_reports.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve all global suppressions #
# GET /suppression/unsubscribes #

params = {'start_time': 1, 'limit': 1, 'end_time': 1, 'offset': 1}
response = sg.client.suppression.unsubscribes.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

