import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient()

##################################################
# Create a Custom Field #
# POST /contactdb/custom_fields #

data = {'sample': 'data'}
response = sg.client.contactdb.custom_fields.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# List All Custom Fields #
# GET /contactdb/custom_fields #

response = sg.client.contactdb.custom_fields.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get a Custom Field #
# GET /contactdb/custom_fields/{custom_field_id} #

params = {'custom_field_id': 0}
custom_field_id = "test_url_param"
response = sg.client.contactdb.custom_fields._(custom_field_id).get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a Custom Field #
# DELETE /contactdb/custom_fields/{custom_field_id} #

custom_field_id = "test_url_param"
response = sg.client.contactdb.custom_fields._(custom_field_id).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Create a List #
# POST /contactdb/lists #

data = {'sample': 'data'}
response = sg.client.contactdb.lists.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# List All Lists #
# GET /contactdb/lists #

response = sg.client.contactdb.lists.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete Multiple lists #
# DELETE /contactdb/lists #

response = sg.client.contactdb.lists.delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update a List #
# PATCH /contactdb/lists/{list_id} #

data = {'sample': 'data'}
params = {'list_id': 0}
list_id = "test_url_param"
response = sg.client.contactdb.lists._(list_id).patch(request_body=data, query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get a single list. #
# GET /contactdb/lists/{list_id} #

params = {'list_id': 0}
list_id = "test_url_param"
response = sg.client.contactdb.lists._(list_id).get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a List #
# DELETE /contactdb/lists/{list_id} #

params = {'delete_contacts': 0}
list_id = "test_url_param"
response = sg.client.contactdb.lists._(list_id).delete(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Add Multiple Recipients to a List #
# POST /contactdb/lists/{list_id}/recipients #

data = {'sample': 'data'}
params = {'list_id': 0}
list_id = "test_url_param"
response = sg.client.contactdb.lists._(list_id).recipients.post(request_body=data, query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# List Recipients on a List #
# GET /contactdb/lists/{list_id}/recipients #

params = {'page': 0, 'page_size': 0, 'list_id': 0}
list_id = "test_url_param"
response = sg.client.contactdb.lists._(list_id).recipients.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Add a Single Recipient to a List #
# POST /contactdb/lists/{list_id}/recipients/{recipient_id} #

data = {'sample': 'data'}
params = {'recipient_id': 'test_string', 'list_id': 0}
list_id = "test_url_param"
        recipient_id = "test_url_param"
response = sg.client.contactdb.lists._(list_id).recipients._(recipient_id).post(request_body=data, query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a Single Recipient from a Single List #
# DELETE /contactdb/lists/{list_id}/recipients/{recipient_id} #

params = {'recipient_id': 0, 'list_id': 0}
list_id = "test_url_param"
        recipient_id = "test_url_param"
response = sg.client.contactdb.lists._(list_id).recipients._(recipient_id).delete(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update Recipient #
# PATCH /contactdb/recipients #

data = {'sample': 'data'}
response = sg.client.contactdb.recipients.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Add recipients #
# POST /contactdb/recipients #

data = {'sample': 'data'}
response = sg.client.contactdb.recipients.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# List Recipients [waiting on Bryan Adamson's response] #
# GET /contactdb/recipients #

params = {'page': 0, 'page_size': 0}
response = sg.client.contactdb.recipients.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete Recipient #
# DELETE /contactdb/recipients #

response = sg.client.contactdb.recipients.delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get the count of billable recipients #
# GET /contactdb/recipients/billable_count #

response = sg.client.contactdb.recipients.billable_count.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get a Count of Recipients #
# GET /contactdb/recipients/count #

response = sg.client.contactdb.recipients.count.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get Recipients Matching Search Criteria #
# GET /contactdb/recipients/search #

params = {'{field_name}': 'test_string'}
response = sg.client.contactdb.recipients.search.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve a single recipient #
# GET /contactdb/recipients/{recipient_id} #

params = {'recipient_id': 'test_string'}
recipient_id = "test_url_param"
response = sg.client.contactdb.recipients._(recipient_id).get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a Recipient #
# DELETE /contactdb/recipients/{recipient_id} #

params = {'recipient_id': 'test_string'}
recipient_id = "test_url_param"
response = sg.client.contactdb.recipients._(recipient_id).delete(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get the Lists the Recipient Is On #
# GET /contactdb/recipients/{recipient_id}/lists #

params = {'recipient_id': 'test_string'}
recipient_id = "test_url_param"
response = sg.client.contactdb.recipients._(recipient_id).lists.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get reserved custom fields fields. #
# GET /contactdb/reserved_fields #

response = sg.client.contactdb.reserved_fields.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Create a Segment #
# POST /contactdb/segments #

data = {'sample': 'data'}
response = sg.client.contactdb.segments.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# List All Segments #
# GET /contactdb/segments #

response = sg.client.contactdb.segments.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update a segment #
# PATCH /contactdb/segments/{segment_id} #

data = {'sample': 'data'}
params = {'segment_id': 'test_string'}
segment_id = "test_url_param"
response = sg.client.contactdb.segments._(segment_id).patch(request_body=data, query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve a Segment #
# GET /contactdb/segments/{segment_id} #

params = {'segment_id': 0}
segment_id = "test_url_param"
response = sg.client.contactdb.segments._(segment_id).get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a Segment #
# DELETE /contactdb/segments/{segment_id} #

params = {'delete_contacts': 0}
segment_id = "test_url_param"
response = sg.client.contactdb.segments._(segment_id).delete(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# List Recipients On a Segment #
# GET /contactdb/segments/{segment_id}/recipients #

params = {'page': 0, 'page_size': 0}
segment_id = "test_url_param"
response = sg.client.contactdb.segments._(segment_id).recipients.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

