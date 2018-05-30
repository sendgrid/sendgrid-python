import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

##################################################
# Create a new suppression group #
# POST /asm/groups #

data = {
    "description": "Suggestions for products our users might like.",
    "is_default": True,
    "name": "Product Suggestions"
}
response = sg.client.asm.groups.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve information about multiple suppression groups #
# GET /asm/groups #

params = {'id': 1}
response = sg.client.asm.groups.get(query_params=params)
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
response = sg.client.asm.groups._(
    group_id).suppressions.post(request_body=data)
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
# Search for suppressions within a group #
# POST /asm/groups/{group_id}/suppressions/search #

data = {
    "recipient_emails": [
        "exists1@example.com",
        "exists2@example.com",
        "doesnotexists@example.com"
    ]
}
group_id = "test_url_param"
response = sg.client.asm.groups._(
    group_id).suppressions.search.post(request_body=data)
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
# Retrieve all suppressions #
# GET /asm/suppressions #

response = sg.client.asm.suppressions.get()
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

##################################################
# Retrieve all suppression groups for an email address #
# GET /asm/suppressions/{email} #

email = "test_url_param"
response = sg.client.asm.suppressions._(email).get()
print(response.status_code)
print(response.body)
print(response.headers)
