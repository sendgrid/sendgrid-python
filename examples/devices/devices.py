import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

##################################################
# Retrieve email statistics by device type. #
# GET /devices/stats #

params = {'aggregated_by': 'day', 'limit': 1,
          'start_date': '2016-01-01',
          'end_date': '2016-04-01',
          'offset': 1}
response = sg.client.devices.stats.get(query_params=params)
print(response.status_code)
print(response.body)
print(response.headers)
