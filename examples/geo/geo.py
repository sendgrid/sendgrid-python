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
# Retrieve email statistics by country and state/province. #
# GET /geo/stats #

params = {'end_date': 'test_string', 'country': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'offset': 0, 'start_date': 'test_string'}
response = self.sg.client.geo.stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

