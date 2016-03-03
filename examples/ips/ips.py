import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# List all IPs #
# GET /ips #

params = {'subuser': 'test_string', 'ip': 'test_string', 'limit': 0, 'exclude_whitelabels': 0, 'offset': 0}
response = sg.client.ips.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# List all assigned IPs #
# GET /ips/assigned #

response = sg.client.ips.assigned.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Create an IP pool. #
# POST /ips/pools #

data = {'sample': 'data'}
response = sg.client.ips.pools.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# List all IP pools. #
# GET /ips/pools #

response = sg.client.ips.pools.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update an IP pools name. #
# PUT /ips/pools/{pool_name} #

data = {'sample': 'data'}
pool_name = "test_url_param"
response = sg.client.ips.pools._(pool_name).put(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# List the IPs in a specified pool. #
# GET /ips/pools/{pool_name} #

pool_name = "test_url_param"
response = sg.client.ips.pools._(pool_name).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete an IP pool. #
# DELETE /ips/pools/{pool_name} #

pool_name = "test_url_param"
response = sg.client.ips.pools._(pool_name).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Add an IP to a pool #
# POST /ips/pools/{pool_name}/ips #

data = {'sample': 'data'}
pool_name = "test_url_param"
response = sg.client.ips.pools._(pool_name).ips.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Remove an IP address from a pool. #
# DELETE /ips/pools/{pool_name}/ips/{ip} #

pool_name = "test_url_param"
        ip = "test_url_param"
response = sg.client.ips.pools._(pool_name).ips._(ip).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Add an IP to warmup. #
# POST /ips/warmup #

data = {'sample': 'data'}
response = sg.client.ips.warmup.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get all IPs that are currently warming up. #
# GET /ips/warmup #

response = sg.client.ips.warmup.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get warmup status for a particular IP. #
# GET /ips/warmup/{ip_address} #

ip_address = "test_url_param"
response = sg.client.ips.warmup._(ip_address).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Remove an IP from warmup. #
# DELETE /ips/warmup/{ip_address} #

ip_address = "test_url_param"
response = sg.client.ips.warmup._(ip_address).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# See which pools an IP address belongs to. #
# GET /ips/{ip_address} #

ip_address = "test_url_param"
response = sg.client.ips._(ip_address).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

