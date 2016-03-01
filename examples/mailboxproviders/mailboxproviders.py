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
# Retrieve email statistics by mailbox provider. #
# GET /mailbox_providers/stats #

params = {'end_date': 'test_string', 'mailbox_providers': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'offset': 0, 'start_date': 'test_string'}
response = self.sg.client.mailbox_providers.stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

