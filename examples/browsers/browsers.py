import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient()

##################################################
# Retrieve email statistics by browser.  #
# GET /browsers/stats #

params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'browsers': 'test_string', 'limit': 'test_string', 'offset': 'test_string', 'start_date': 'test_string'}
response = sg.client.browsers.stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

