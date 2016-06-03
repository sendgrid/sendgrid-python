import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

##################################################
# Create a Group #
# POST /asm/groups #

data = {
  "description": "A group description", 
  "is_default": False, 
  "name": "A group name"
}
response = sg.client.asm.groups.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve all suppression groups associated with the user. #
# GET /asm/groups #

response = sg.client.asm.groups.get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Update a suppression group. #
# PATCH /asm/groups/{group_id} #

data = {
  "description": "Suggestions for items our users might like.", 
  "id": 103, 
  "name": "Item Suggestions"
}
group_id = "test_url_param"
response = sg.client.asm.groups._(group_id).patch(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Get information on a single suppression group. #
# GET /asm/groups/{group_id} #

group_id = "test_url_param"
response = sg.client.asm.groups._(group_id).get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Delete a suppression group. #
# DELETE /asm/groups/{group_id} #

group_id = "test_url_param"
response = sg.client.asm.groups._(group_id).delete()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Add suppressions to a suppression group #
# POST /asm/groups/{group_id}/suppressions #

data = {
  "recipient_emails": [
    "test1@example.com", 
    "test2@example.com"
  ]
}
group_id = "test_url_param"
response = sg.client.asm.groups._(group_id).suppressions.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve all suppressions for a suppression group #
# GET /asm/groups/{group_id}/suppressions #

group_id = "test_url_param"
response = sg.client.asm.groups._(group_id).suppressions.get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Delete a suppression from a suppression group #
# DELETE /asm/groups/{group_id}/suppressions/{email} #

group_id = "test_url_param"
        email = "test_url_param"
response = sg.client.asm.groups._(group_id).suppressions._(email).delete()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Add recipient addresses to the global suppression group. #
# POST /asm/suppressions/global #

data = {
  "recipient_emails": [
    "test1@example.com", 
    "test2@example.com"
  ]
}
response = sg.client.asm.suppressions._("global").post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve a Global Suppression #
# GET /asm/suppressions/global/{email} #

email = "test_url_param"
response = sg.client.asm.suppressions._("global")._(email).get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Delete a Global Suppression #
# DELETE /asm/suppressions/global/{email} #

email = "test_url_param"
response = sg.client.asm.suppressions._("global")._(email).delete()
print(response.status_code)
print(response.body)
print(response.headers)

