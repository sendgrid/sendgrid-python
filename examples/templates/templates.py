import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient()

##################################################
# Create a transactional template. #
# POST /templates #

data = {'sample': 'data'}
response = sg.client.templates.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve all transactional templates. #
# GET /templates #

response = sg.client.templates.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Edit a transactional template. #
# PATCH /templates/{template_id} #

data = {'sample': 'data'}
template_id = "test_url_param"
response = sg.client.templates._(template_id).patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve a single transactional template. #
# GET /templates/{template_id} #

template_id = "test_url_param"
response = sg.client.templates._(template_id).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a template. #
# DELETE /templates/{template_id} #

template_id = "test_url_param"
response = sg.client.templates._(template_id).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Create a new transactional template version. #
# POST /templates/{template_id}/versions #

data = {'sample': 'data'}
template_id = "test_url_param"
response = sg.client.templates._(template_id).versions.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Edit a transactional template version. #
# PATCH /templates/{template_id}/versions/{version_id} #

data = {'sample': 'data'}
template_id = "test_url_param"
        version_id = "test_url_param"
response = sg.client.templates._(template_id).versions._(version_id).patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve a specific transactional template version. #
# GET /templates/{template_id}/versions/{version_id} #

template_id = "test_url_param"
        version_id = "test_url_param"
response = sg.client.templates._(template_id).versions._(version_id).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a transactional template version. #
# DELETE /templates/{template_id}/versions/{version_id} #

template_id = "test_url_param"
        version_id = "test_url_param"
response = sg.client.templates._(template_id).versions._(version_id).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Activate a transactional template version. #
# POST /templates/{template_id}/versions/{version_id}/activate #

data = {'sample': 'data'}
template_id = "test_url_param"
        version_id = "test_url_param"
response = sg.client.templates._(template_id).versions._(version_id).activate.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

