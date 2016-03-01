import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient()

##################################################
# Create a Campaign #
# POST /campaigns #

data = {'sample': 'data'}
response = sg.client.campaigns.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get all Campaigns #
# GET /campaigns #

params = {'limit': 0, 'offset': 0}
response = sg.client.campaigns.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update a Campaign #
# PATCH /campaigns/{campaign_id} #

data = {'sample': 'data'}
campaign_id = "test_url_param"
response = sg.client.campaigns._(campaign_id).patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get a single campaign #
# GET /campaigns/{campaign_id} #

campaign_id = "test_url_param"
response = sg.client.campaigns._(campaign_id).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a Campaign #
# DELETE /campaigns/{campaign_id} #

campaign_id = "test_url_param"
response = sg.client.campaigns._(campaign_id).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update a Scheduled Campaign #
# PATCH /campaigns/{campaign_id}/schedules #

data = {'sample': 'data'}
campaign_id = "test_url_param"
response = sg.client.campaigns._(campaign_id).schedules.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Schedule a Campaign #
# POST /campaigns/{campaign_id}/schedules #

data = {'sample': 'data'}
campaign_id = "test_url_param"
response = sg.client.campaigns._(campaign_id).schedules.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# View Scheduled Time of a Campaign #
# GET /campaigns/{campaign_id}/schedules #

campaign_id = "test_url_param"
response = sg.client.campaigns._(campaign_id).schedules.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Unschedule a Scheduled Campaign #
# DELETE /campaigns/{campaign_id}/schedules #

campaign_id = "test_url_param"
response = sg.client.campaigns._(campaign_id).schedules.delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Send a Campaign #
# POST /campaigns/{campaign_id}/schedules/now #

data = {'sample': 'data'}
campaign_id = "test_url_param"
response = sg.client.campaigns._(campaign_id).schedules.now.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Send a Test Campaign #
# POST /campaigns/{campaign_id}/schedules/test #

data = {'sample': 'data'}
campaign_id = "test_url_param"
response = sg.client.campaigns._(campaign_id).schedules.test.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

