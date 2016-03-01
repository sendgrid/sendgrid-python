import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient()

##################################################
# Retrieve email statistics by client type. #
# GET /clients/stats #

params = {'aggregated_by': 'test_string', 'start_date': 'test_string', 'end_date': 'test_string'}
response = sg.client.clients.stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve stats by a specific client type. #
# GET /clients/{client_type}/stats #

params = {'aggregated_by': 'test_string', 'start_date': 'test_string', 'end_date': 'test_string'}
client_type = "test_url_param"
response = sg.client.clients._(client_type).stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

