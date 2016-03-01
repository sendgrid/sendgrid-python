import sendgrid
import os
sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
host = os.environ.get('HOST') # e.g. https://api.sendgrid.com
request_headers = {
    "Authorization": 'Bearer {0}'.format(sendgrid_api_key),
    "Content-Type": "application/json"
}
sg = sendgrid.SendGridAPIClient(host=host, request_headers=request_headers)

##################################################
# Create Subuser #
# POST /subusers #

data = {'sample': 'data'}
response = self.sg.client.subusers.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# List all Subusers #
# GET /subusers #

params = {'username': 'test_string', 'limit': 0, 'offset': 0}
response = self.sg.client.subusers.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve Subuser Reputations #
# GET /subusers/reputations #

params = {'usernames': 'test_string'}
response = self.sg.client.subusers.reputations.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve email statistics for your subusers. #
# GET /subusers/stats #

params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'offset': 0, 'start_date': 'test_string', 'subusers': 'test_string'}
response = self.sg.client.subusers.stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
#  Retrieve the totals for each email statistic metric for all subusers. #
# GET /subusers/stats/sums #

params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'sort_by_metric': 'test_string', 'offset': 0, 'start_date': 'test_string', 'sort_by_direction': 'test_string'}
response = self.sg.client.subusers.stats.sums.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Enable/disable a subuser #
# PATCH /subusers/{subuser_name} #

data = {'sample': 'data'}
subuser_name = "test_url_param"
response = self.sg.client.subusers._(subuser_name).patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a subuser #
# DELETE /subusers/{subuser_name} #

subuser_name = "test_url_param"
response = self.sg.client.subusers._(subuser_name).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update IPs assigned to a subuser #
# PUT /subusers/{subuser_name}/ips #

data = {'sample': 'data'}
subuser_name = "test_url_param"
response = self.sg.client.subusers._(subuser_name).ips.put(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update Monitor Settings for a subuser #
# PUT /subusers/{subuser_name}/monitor #

data = {'sample': 'data'}
subuser_name = "test_url_param"
response = self.sg.client.subusers._(subuser_name).monitor.put(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Create monitor settings #
# POST /subusers/{subuser_name}/monitor #

data = {'sample': 'data'}
subuser_name = "test_url_param"
response = self.sg.client.subusers._(subuser_name).monitor.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve monitor settings for a subuser #
# GET /subusers/{subuser_name}/monitor #

subuser_name = "test_url_param"
response = self.sg.client.subusers._(subuser_name).monitor.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete monitor settings #
# DELETE /subusers/{subuser_name}/monitor #

subuser_name = "test_url_param"
response = self.sg.client.subusers._(subuser_name).monitor.delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

