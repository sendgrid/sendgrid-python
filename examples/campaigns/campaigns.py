import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# Create a Campaign #
# POST /campaigns #

data = {
  "categories": [
    "spring line"
  ], 
  "custom_unsubscribe_url": "", 
  "html_content": "<html><head><title></title></head><body><p>Check out our spring line!</p></body></html>", 
  "ip_pool": "marketing", 
  "list_ids": [
    110, 
    124
  ], 
  "plain_content": "Check out our spring line!", 
  "segment_ids": [
    110
  ], 
  "sender_id": 124451, 
  "subject": "New Products for Spring!", 
  "suppression_group_id": 42, 
  "title": "March Newsletter"
}
response = sg.client.campaigns.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve all Campaigns #
# GET /campaigns #

params = {'limit': 0, 'offset': 0}
response = sg.client.campaigns.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update a Campaign #
# PATCH /campaigns/{campaign_id} #

data = {
  "categories": [
    "summer line"
  ], 
  "html_content": "<html><head><title></title></head><body><p>Check out our summer line!</p></body></html>", 
  "plain_content": "Check out our summer line!", 
  "subject": "New Products for Summer!", 
  "title": "May Newsletter"
}
campaign_id = "test_url_param"
response = sg.client.campaigns._(campaign_id).patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve a single campaign #
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
# Unschedule a Scheduled Campaign #
# DELETE /campaigns/{campaign_id}/schedules #

campaign_id = "test_url_param"
response = sg.client.campaigns._(campaign_id).schedules.delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Schedule a Campaign #
# POST /campaigns/{campaign_id}/schedules #

data = {
  "send_at": 1489771528
}
campaign_id = "test_url_param"
response = sg.client.campaigns._(campaign_id).schedules.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update a Scheduled Campaign #
# PATCH /campaigns/{campaign_id}/schedules #

campaign_id = "test_url_param"
response = sg.client.campaigns._(campaign_id).schedules.patch()
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
# Send a Campaign #
# POST /campaigns/{campaign_id}/schedules/now #

campaign_id = "test_url_param"
response = sg.client.campaigns._(campaign_id).schedules.now.post()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Send a Test Campaign #
# POST /campaigns/{campaign_id}/schedules/test #

data = {
  "to": "your.email@example.com"
}
campaign_id = "test_url_param"
response = sg.client.campaigns._(campaign_id).schedules.test.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

