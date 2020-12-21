import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

##################################################
# Create a domain authentication. #
# POST /whitelabel/domains #

data = {
    "automatic_security": False,
    "custom_spf": True,
    "default": True,
    "domain": "example.com",
    "ips": [
        "192.168.1.1",
        "192.168.1.2"
    ],
    "subdomain": "news",
    "username": "john@example.com"
}
response = sg.client.whitelabel.domains.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# List all domain authentications. #
# GET /whitelabel/domains #

params = {'username': 'test_string', 'domain': 'test_string',
          'exclude_subusers': 'true', 'limit': 1, 'offset': 1}
response = sg.client.whitelabel.domains.get(query_params=params)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Get the default domain authentication. #
# GET /whitelabel/domains/default #

response = sg.client.whitelabel.domains.default.get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# List the domain authentication associated with the given user. #
# GET /whitelabel/domains/subuser #

response = sg.client.whitelabel.domains.subuser.get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Disassociate a domain authentication from a given user. #
# DELETE /whitelabel/domains/subuser #

response = sg.client.whitelabel.domains.subuser.delete()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Update a domain authentication. #
# PATCH /whitelabel/domains/{domain_id} #

data = {
    "custom_spf": True,
    "default": False
}
domain_id = "test_url_param"
response = sg.client.whitelabel.domains._(domain_id).patch(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve a domain authentication. #
# GET /whitelabel/domains/{domain_id} #

domain_id = "test_url_param"
response = sg.client.whitelabel.domains._(domain_id).get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Delete a domain authentication. #
# DELETE /whitelabel/domains/{domain_id} #

domain_id = "test_url_param"
response = sg.client.whitelabel.domains._(domain_id).delete()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Associate a domain authentication with a given user. #
# POST /whitelabel/domains/{domain_id}/subuser #

data = {
    "username": "jane@example.com"
}
domain_id = "test_url_param"
response = sg.client.whitelabel.domains._(
    domain_id).subuser.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Add an IP to a domain authentication. #
# POST /whitelabel/domains/{id}/ips #

data = {
    "ip": "192.168.0.1"
}
id_ = "test_url_param"
response = sg.client.whitelabel.domains._(id_).ips.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Remove an IP from a domain authentication. #
# DELETE /whitelabel/domains/{id}/ips/{ip} #

id_ = "test_url_param"
ip = "test_url_param"
response = sg.client.whitelabel.domains._(id_).ips._(ip).delete()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Validate a domain authentication. #
# POST /whitelabel/domains/{id}/validate #

id_ = "test_url_param"
response = sg.client.whitelabel.domains._(id_).validate.post()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Create a reverse DNS record #
# POST /whitelabel/ips #

data = {
    "domain": "example.com",
    "ip": "192.168.1.1",
    "subdomain": "email"
}
response = sg.client.whitelabel.ips.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Create a reverse DNS record #
# GET /whitelabel/ips #

params = {'ip': 'test_string', 'limit': 1, 'offset': 1}
response = sg.client.whitelabel.ips.get(query_params=params)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve a reverse DNS record #
# GET /whitelabel/ips/{id} #

id_ = "test_url_param"
response = sg.client.whitelabel.ips._(id_).get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Delete a reverse DNS record #
# DELETE /whitelabel/ips/{id} #

id_ = "test_url_param"
response = sg.client.whitelabel.ips._(id_).delete()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Validate a reverse DNS record #
# POST /whitelabel/ips/{id}/validate #

id_ = "test_url_param"
response = sg.client.whitelabel.ips._(id_).validate.post()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Create a Link Branding #
# POST /whitelabel/links #

data = {
    "default": True,
    "domain": "example.com",
    "subdomain": "mail"
}
params = {'limit': 1, 'offset': 1}
response = sg.client.whitelabel.links.post(
    request_body=data, query_params=params)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve all link brandings #
# GET /whitelabel/links #

params = {'limit': 1}
response = sg.client.whitelabel.links.get(query_params=params)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve a Default Link Branding #
# GET /whitelabel/links/default #

params = {'domain': 'test_string'}
response = sg.client.whitelabel.links.default.get(query_params=params)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve Associated Link Branding #
# GET /whitelabel/links/subuser #

params = {'username': 'test_string'}
response = sg.client.whitelabel.links.subuser.get(query_params=params)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Disassociate a Link Branding #
# DELETE /whitelabel/links/subuser #

params = {'username': 'test_string'}
response = sg.client.whitelabel.links.subuser.delete(query_params=params)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Update a Link Branding #
# PATCH /whitelabel/links/{id} #

data = {
    "default": True
}
id_ = "test_url_param"
response = sg.client.whitelabel.links._(id_).patch(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve a Link Branding #
# GET /whitelabel/links/{id} #

id_ = "test_url_param"
response = sg.client.whitelabel.links._(id_).get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Delete a Link Branding #
# DELETE /whitelabel/links/{id} #

id_ = "test_url_param"
response = sg.client.whitelabel.links._(id_).delete()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Validate a Link Branding #
# POST /whitelabel/links/{id}/validate #

id_ = "test_url_param"
response = sg.client.whitelabel.links._(id_).validate.post()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Associate a Link Branding #
# POST /whitelabel/links/{link_id}/subuser #

data = {
    "username": "jane@example.com"
}
link_id = "test_url_param"
response = sg.client.whitelabel.links._(
    link_id).subuser.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)
