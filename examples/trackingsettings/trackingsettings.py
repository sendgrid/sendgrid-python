import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

##################################################
# Retrieve Tracking Settings #
# GET /tracking_settings #

params = {'limit': 1, 'offset': 1}
response = sg.client.tracking_settings.get(query_params=params)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Update Click Tracking Settings #
# PATCH /tracking_settings/click #

data = {
    "enabled": True
}
response = sg.client.tracking_settings.click.patch(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve Click Track Settings #
# GET /tracking_settings/click #

response = sg.client.tracking_settings.click.get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Update Google Analytics Settings #
# PATCH /tracking_settings/google_analytics #

data = {
    "enabled": True,
    "utm_campaign": "website",
    "utm_content": "",
    "utm_medium": "email",
    "utm_source": "sendgrid.com",
    "utm_term": ""
}
response = sg.client.tracking_settings.google_analytics.patch(
    request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve Google Analytics Settings #
# GET /tracking_settings/google_analytics #

response = sg.client.tracking_settings.google_analytics.get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Update Open Tracking Settings #
# PATCH /tracking_settings/open #

data = {
    "enabled": True
}
response = sg.client.tracking_settings.open.patch(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Get Open Tracking Settings #
# GET /tracking_settings/open #

response = sg.client.tracking_settings.open.get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Update Subscription Tracking Settings #
# PATCH /tracking_settings/subscription #

data = {
    "enabled": True,
    "html_content": "html content",
    "landing": "landing page html",
    "plain_content": "text content",
    "replace": "replacement tag",
    "url": "url"
}
response = sg.client.tracking_settings.subscription.patch(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve Subscription Tracking Settings #
# GET /tracking_settings/subscription #

response = sg.client.tracking_settings.subscription.get()
print(response.status_code)
print(response.body)
print(response.headers)
