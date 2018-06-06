import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

##################################################
# Retrieve all recent access attempts #
# GET /access_settings/activity #

params = {'limit': 1}
response = sg.client.access_settings.activity.get(query_params=params)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Add one or more IPs to the whitelist #
# POST /access_settings/whitelist #

data = {
    "ips": [
        {
            "ip": "192.168.1.1"
        },
        {
            "ip": "192.*.*.*"
        },
        {
            "ip": "192.168.1.3/32"
        }
    ]
}
response = sg.client.access_settings.whitelist.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve a list of currently whitelisted IPs #
# GET /access_settings/whitelist #

response = sg.client.access_settings.whitelist.get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Remove one or more IPs from the whitelist #
# DELETE /access_settings/whitelist #

data = {
    "ids": [
        1,
        2,
        3
    ]
}
response = sg.client.access_settings.whitelist.delete(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve a specific whitelisted IP #
# GET /access_settings/whitelist/{rule_id} #

rule_id = "test_url_param"
response = sg.client.access_settings.whitelist._(rule_id).get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Remove a specific IP from the whitelist #
# DELETE /access_settings/whitelist/{rule_id} #

rule_id = "test_url_param"
response = sg.client.access_settings.whitelist._(rule_id).delete()
print(response.status_code)
print(response.body)
print(response.headers)
