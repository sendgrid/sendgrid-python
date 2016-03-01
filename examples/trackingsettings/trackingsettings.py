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
# Get Tracking Settings #
# GET /tracking_settings #

params = {'limit': 0, 'offset': 0}
response = self.sg.client.tracking_settings.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update Click Tracking Settings #
# PATCH /tracking_settings/click #

data = {'sample': 'data'}
response = self.sg.client.tracking_settings.click.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get Click Track Settings #
# GET /tracking_settings/click #

response = self.sg.client.tracking_settings.click.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update Google Analytics Settings #
# PATCH /tracking_settings/google_analytics #

data = {'sample': 'data'}
response = self.sg.client.tracking_settings.google_analytics.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get Google Analytics Settings #
# GET /tracking_settings/google_analytics #

response = self.sg.client.tracking_settings.google_analytics.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update Open Tracking Settings #
# PATCH /tracking_settings/open #

data = {'sample': 'data'}
response = self.sg.client.tracking_settings.open.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get Open Tracking Settings #
# GET /tracking_settings/open #

response = self.sg.client.tracking_settings.open.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update Subscription Tracking Settings #
# PATCH /tracking_settings/subscription #

data = {'sample': 'data'}
response = self.sg.client.tracking_settings.subscription.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get Subscription Tracking Settings #
# GET /tracking_settings/subscription #

response = self.sg.client.tracking_settings.subscription.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

