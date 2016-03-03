import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# Create a Group #
# POST /asm/groups #

data = {'sample': 'data'}
response = sg.client.asm.groups.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve all suppression groups associated with the user. #
# GET /asm/groups #

response = sg.client.asm.groups.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update a suppression group. #
# PATCH /asm/groups/{group_id} #

data = {'sample': 'data'}
group_id = "test_url_param"
response = sg.client.asm.groups._(group_id).patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get information on a single suppression group. #
# GET /asm/groups/{group_id} #

group_id = "test_url_param"
response = sg.client.asm.groups._(group_id).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a suppression group. #
# DELETE /asm/groups/{group_id} #

group_id = "test_url_param"
response = sg.client.asm.groups._(group_id).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Add suppressions to a suppression group #
# POST /asm/groups/{group_id}/suppressions #

data = {'sample': 'data'}
group_id = "test_url_param"
response = sg.client.asm.groups._(group_id).suppressions.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve all suppressions for a suppression group #
# GET /asm/groups/{group_id}/suppressions #

group_id = "test_url_param"
response = sg.client.asm.groups._(group_id).suppressions.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a suppression from a suppression group #
# DELETE /asm/groups/{group_id}/suppressions/{email} #

group_id = "test_url_param"
        email = "test_url_param"
response = sg.client.asm.groups._(group_id).suppressions._(email).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Add recipient addresses to the global suppression group. #
# POST /asm/suppressions/global #

data = {'sample': 'data'}
response = sg.client.asm.suppressions._("global").post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Check if a recipient address is in the global suppressions group. #
# GET /asm/suppressions/global/{email_address} #

email_address = "test_url_param"
response = sg.client.asm.suppressions._("global")._(email_address).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve a Global Suppression #
# GET /asm/suppressions/global/{email} #

email = "test_url_param"
response = sg.client.asm.suppressions._("global")._(email).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a Global Suppression #
# DELETE /asm/suppressions/global/{email} #

email = "test_url_param"
response = sg.client.asm.suppressions._("global")._(email).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

