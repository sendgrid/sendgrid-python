import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# Retrieve email statistics by mailbox provider. #
# GET /mailbox_providers/stats #

params = {'end_date': 'test_string', 'mailbox_providers': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'offset': 0, 'start_date': 'test_string'}
response = sg.client.mailbox_providers.stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

