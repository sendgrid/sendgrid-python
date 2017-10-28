import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

##################################################
# Retrieve email statistics by client type. #
# GET /clients/stats #

params = {'aggregated_by': 'day',
          'start_date': '2016-01-01',
          'end_date': '2016-04-01'}
response = sg.client.clients.stats.get(query_params=params)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve stats by a specific client type. #
# GET /clients/{client_type}/stats #

params = {'aggregated_by': 'day',
          'start_date': '2016-01-01',
          'end_date': '2016-04-01'}
client_type = "test_url_param"
response = sg.client.clients._(client_type).stats.get(query_params=params)
print(response.status_code)
print(response.body)
print(response.headers)
