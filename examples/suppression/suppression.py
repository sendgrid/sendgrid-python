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
# List all bounces #
# GET /suppression/bounces #

params = {'start_time': 0, 'end_time': 0}
response = self.sg.client.suppression.bounces.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete bounces #
# DELETE /suppression/bounces #

response = self.sg.client.suppression.bounces.delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get a Bounce #
# GET /suppression/bounces/{email} #

email = "test_url_param"
response = self.sg.client.suppression.bounces._(email).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a bounce #
# DELETE /suppression/bounces/{email} #

params = {'email_address': 'test_string'}
email = "test_url_param"
response = self.sg.client.suppression.bounces._(email).delete(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

