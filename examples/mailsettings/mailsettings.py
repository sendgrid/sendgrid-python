import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

##################################################
# Retrieve all mail settings #
# GET /mail_settings #

params = {'limit': 1, 'offset': 1}
response = sg.client.mail_settings.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update address whitelist mail settings #
# PATCH /mail_settings/address_whitelist #

data = {
  "enabled": true, 
  "list": [
    "email1@example.com", 
    "example.com"
  ]
}
response = sg.client.mail_settings.address_whitelist.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve address whitelist mail settings #
# GET /mail_settings/address_whitelist #

response = sg.client.mail_settings.address_whitelist.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update BCC mail settings #
# PATCH /mail_settings/bcc #

data = {
  "email": "email@example.com", 
  "enabled": false
}
response = sg.client.mail_settings.bcc.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve all BCC mail settings #
# GET /mail_settings/bcc #

response = sg.client.mail_settings.bcc.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve bounce purge mail settings #
# GET /mail_settings/bounce_purge #

response = sg.client.mail_settings.bounce_purge.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update bounce purge mail settings #
# PATCH /mail_settings/bounce_purge #

data = {
  "enabled": true, 
  "hard_bounces": 5, 
  "soft_bounces": 5
}
response = sg.client.mail_settings.bounce_purge.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update footer mail settings #
# PATCH /mail_settings/footer #

data = {
  "enabled": true, 
  "html_content": "...", 
  "plain_content": "..."
}
response = sg.client.mail_settings.footer.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve footer mail settings #
# GET /mail_settings/footer #

response = sg.client.mail_settings.footer.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve forward bounce mail settings #
# GET /mail_settings/forward_bounce #

response = sg.client.mail_settings.forward_bounce.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update forward bounce mail settings #
# PATCH /mail_settings/forward_bounce #

data = {
  "email": "example@example.com", 
  "enabled": true
}
response = sg.client.mail_settings.forward_bounce.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve forward spam mail settings #
# GET /mail_settings/forward_spam #

response = sg.client.mail_settings.forward_spam.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update forward spam mail settings #
# PATCH /mail_settings/forward_spam #

data = {
  "email": "", 
  "enabled": false
}
response = sg.client.mail_settings.forward_spam.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update plain content mail settings #
# PATCH /mail_settings/plain_content #

data = {
  "enabled": false
}
response = sg.client.mail_settings.plain_content.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve plain content mail settings #
# GET /mail_settings/plain_content #

response = sg.client.mail_settings.plain_content.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update spam check mail settings #
# PATCH /mail_settings/spam_check #

data = {
  "enabled": true, 
  "max_score": 5, 
  "url": "url"
}
response = sg.client.mail_settings.spam_check.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve spam check mail settings #
# GET /mail_settings/spam_check #

response = sg.client.mail_settings.spam_check.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update template mail settings #
# PATCH /mail_settings/template #

data = {
  "enabled": true, 
  "html_content": "<% body %>"
}
response = sg.client.mail_settings.template.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve legacy template mail settings #
# GET /mail_settings/template #

response = sg.client.mail_settings.template.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

