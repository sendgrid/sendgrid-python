import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# Retrieve email statistics by browser.  #
# GET /browsers/stats #

params = {'end_date': '2016-04-01', 'aggregated_by': 'day', 'browsers': 'test_string', 'limit': 'test_string', 'offset': 'test_string', 'start_date': '2016-01-01'}
response = sg.client.browsers.stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

