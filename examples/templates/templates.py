import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

##################################################
# Create a transactional template. #
# POST /templates #

data = {
  "name": "example_name"
}
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

data = {
  "name": "new_example_name"
}
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

data = {
  "active": 1, 
  "html_content": "<%body%>", 
  "name": "example_version_name", 
  "plain_content": "<%body%>", 
  "subject": "<%subject%>", 
  "template_id": "ddb96bbc-9b92-425e-8979-99464621b543"
}
template_id = "test_url_param"
response = sg.client.templates._(template_id).versions.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Edit a transactional template version. #
# PATCH /templates/{template_id}/versions/{version_id} #

data = {
  "active": 1, 
  "html_content": "<%body%>", 
  "name": "updated_example_name", 
  "plain_content": "<%body%>", 
  "subject": "<%subject%>"
}
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

template_id = "test_url_param"
        version_id = "test_url_param"
response = sg.client.templates._(template_id).versions._(version_id).activate.post()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

