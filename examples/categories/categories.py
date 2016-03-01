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
# Get categories #
# GET /categories #

params = {'category': 'test_string', 'sort_by': 'test_string', 'limit': 0, 'order': 'test_string', 'offset': 0}
response = self.sg.client.categories.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve Email Statistics for Categories #
# GET /categories/stats #

params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'offset': 0, 'start_date': 'test_string', 'categories': 'test_string'}
response = self.sg.client.categories.stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve sums of email stats for each category [Needs: Stats object defined, has category ID?] #
# GET /categories/stats/sums #

params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'sort_by_metric': 'test_string', 'offset': 0, 'start_date': 'test_string', 'sort_by_direction': 'test_string'}
response = self.sg.client.categories.stats.sums.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

