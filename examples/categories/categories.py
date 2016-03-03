import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# Get categories #
# GET /categories #

params = {'category': 'test_string', 'sort_by': 'test_string', 'limit': 0, 'order': 'test_string', 'offset': 0}
response = sg.client.categories.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve Email Statistics for Categories #
# GET /categories/stats #

params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'offset': 0, 'start_date': 'test_string', 'categories': 'test_string'}
response = sg.client.categories.stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve sums of email stats for each category [Needs: Stats object defined, has category ID?] #
# GET /categories/stats/sums #

params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'sort_by_metric': 'test_string', 'offset': 0, 'start_date': 'test_string', 'sort_by_direction': 'test_string'}
response = sg.client.categories.stats.sums.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

