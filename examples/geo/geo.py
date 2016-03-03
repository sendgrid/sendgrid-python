import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# Retrieve email statistics by country and state/province. #
# GET /geo/stats #

params = {'end_date': 'test_string', 'country': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'offset': 0, 'start_date': 'test_string'}
response = sg.client.geo.stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

