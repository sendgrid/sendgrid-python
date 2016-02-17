import sendgrid
import json

import os
from sendgrid.config import Config
config = Config()

# StopLight Proxy Test
# https://designer.stoplight.io/wk/F8THnzoqMYoLiWfin/xffLhad2tAAaLiKEq/S5LsAX4SWF7cJHu2R/requests/56b3da76f787db00033b3e18
# sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'), host="https://qpsfwaq3savksegdq.stoplight-proxy.io/v3/")
sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'), host="https://e9sk3d3bfaikbpdq7.stoplight-proxy.io/v3")

data = {"sample": "data"}
params = {"mock": 200}
response = sg.client.asm.suppressions.global_.post(data=data, params=params)
response_json = response.json()
print(response_json)


"""
bounces = sg.client.suppression.bounces
params = {"mock": 200}
response = bounces.get(params=params)
response_json = response.json()
print(response_json)

scopes = sg.client.scopes
response = scopes.get()
response_json = response.json()
scope_data = {"name": "UniversalClient Template Test v3001", "scopes": response_json['scopes'] }

templates = sg.client.templates

# POST Create a template.
data = {"name": "UniversalClient Template Test v3000"}
response = templates.post(data=data)
print(response.status_code)
response_json = response.json()
print(response_json)
template_id = response_json['id']

# GET Retrieve all templates.
response = templates.get()
print(response.status_code)
print(response.json())

# GET Retrieve a single template.
response = templates._(template_id).get()
print(response.status_code)
print(response.json())

# PATCH Edit a template.
data = {"name": "UniversalClient Template Test v3001"}
response = templates._(template_id).patch(data=data)
print(response.status_code)
print(response.json())

# PUT Update the name & scopes of an API Key
response = templates._(template_id).patch(data=scope_data)
print(response.status_code)
print(response.json())

# DELETE Delete a template.
response = templates._(template_id).delete()
print(response.status_code)
"""