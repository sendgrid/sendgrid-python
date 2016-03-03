import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# Retrieve Tracking Settings #
# GET /tracking_settings #

params = {'limit': 0, 'offset': 0}
response = sg.client.tracking_settings.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update Click Tracking Settings #
# PATCH /tracking_settings/click #

data = {'sample': 'data'}
response = sg.client.tracking_settings.click.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve Click Track Settings #
# GET /tracking_settings/click #

response = sg.client.tracking_settings.click.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update Google Analytics Settings #
# PATCH /tracking_settings/google_analytics #

data = {'sample': 'data'}
response = sg.client.tracking_settings.google_analytics.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve Google Analytics Settings #
# GET /tracking_settings/google_analytics #

response = sg.client.tracking_settings.google_analytics.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update Open Tracking Settings #
# PATCH /tracking_settings/open #

data = {'sample': 'data'}
response = sg.client.tracking_settings.open.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get Open Tracking Settings #
# GET /tracking_settings/open #

response = sg.client.tracking_settings.open.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update Subscription Tracking Settings #
# PATCH /tracking_settings/subscription #

data = {'sample': 'data'}
response = sg.client.tracking_settings.subscription.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve Subscription Tracking Settings #
# GET /tracking_settings/subscription #

response = sg.client.tracking_settings.subscription.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

