import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# Retrieve global email statistics #
# GET /stats #

params = {'aggregated_by': 'test_string', 'limit': 0, 'start_date': 'test_string', 'end_date': 'test_string', 'offset': 0}
response = sg.client.stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

