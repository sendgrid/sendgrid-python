import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# Get a user's account information. #
# GET /user/account #

response = sg.client.user.account.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update a user's profile #
# PATCH /user/profile #

data = {'sample': 'data'}
response = sg.client.user.profile.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get a user's profile #
# GET /user/profile #

response = sg.client.user.profile.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Cancel or pause a scheduled send #
# POST /user/scheduled_sends #

data = {'sample': 'data'}
response = sg.client.user.scheduled_sends.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get all scheduled sends #
# GET /user/scheduled_sends #

response = sg.client.user.scheduled_sends.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update user scheduled send information #
# PATCH /user/scheduled_sends/{batch_id} #

data = {'sample': 'data'}
batch_id = "test_url_param"
response = sg.client.user.scheduled_sends._(batch_id).patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve scheduled send #
# GET /user/scheduled_sends/{batch_id} #

batch_id = "test_url_param"
response = sg.client.user.scheduled_sends._(batch_id).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a cancellation or pause of a scheduled send #
# DELETE /user/scheduled_sends/{batch_id} #

batch_id = "test_url_param"
response = sg.client.user.scheduled_sends._(batch_id).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Change the Enforced TLS settings #
# PATCH /user/settings/enforced_tls #

data = {'sample': 'data'}
response = sg.client.user.settings.enforced_tls.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get the current Enforced TLS settings. #
# GET /user/settings/enforced_tls #

response = sg.client.user.settings.enforced_tls.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update Event Notification Settings #
# PATCH /user/webhooks/event/settings #

data = {'sample': 'data'}
response = sg.client.user.webhooks.event.settings.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve Event Webhook Settings #
# GET /user/webhooks/event/settings #

response = sg.client.user.webhooks.event.settings.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Test Event Notification Settings  #
# POST /user/webhooks/event/test #

data = {'sample': 'data'}
response = sg.client.user.webhooks.event.test.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve Parse API settings #
# GET /user/webhooks/parse/settings #

response = sg.client.user.webhooks.parse.settings.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieves Inbound Parse Webhook statistics. #
# GET /user/webhooks/parse/stats #

params = {'aggregated_by': 'test_string', 'limit': 'test_string', 'start_date': 'test_string', 'end_date': 'test_string', 'offset': 'test_string'}
response = sg.client.user.webhooks.parse.stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

