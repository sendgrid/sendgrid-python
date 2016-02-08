import sendgrid
import json

import os
if os.path.exists('.env'):
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

# StopLight Proxy Test
# https://designer.stoplight.io/wk/F8THnzoqMYoLiWfin/xffLhad2tAAaLiKEq/S5LsAX4SWF7cJHu2R/requests/56b3da76f787db00033b3e18
# sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'), host="https://qpsfwaq3savksegdq.stoplight-proxy.io/v3/")
sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

templates = sg.client.templates

#TODO: Do the POST first

# GET Retrieve all templates.
response = templates.get()
print(response.status_code)
print(response.json())

# GET Retrieve a single template.
template_id = "13b8f94f-bcae-4ec6-b752-70d6cb59f932"
response = templates._(template_id).get()
print(response.status_code)
print(response.json())

# POST Create a template.
data = {"name": "UniversalClient Template Test v111"}
response = templates.post(data=data)
print(response.status_code)
response_json = response.json()
print(response_json)
template_id = response_json['id']

# PATCH Edit a template.
data = {"name": "UniversalClient Template Test v222"}
response = templates._(template_id).patch(data=data)
print(response.status_code)
print(response.json())

# DELETE Delete a template.
response = templates._(template_id).delete()
print(response.status_code)