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
# Retrieve email statistics by client type. #
# GET /clients/stats #

params = {'aggregated_by': 'test_string', 'start_date': 'test_string', 'end_date': 'test_string'}
response = self.sg.client.clients.stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve stats by a specific client type. #
# GET /clients/{client_type}/stats #

params = {'aggregated_by': 'test_string', 'start_date': 'test_string', 'end_date': 'test_string'}
client_type = "test_url_param"
response = self.sg.client.clients._(client_type).stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

