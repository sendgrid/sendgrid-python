import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))


##################################################
# Filter all messages #
# GET /messages #

try:
    # Python 3
    from urllib.parse import quote_plus
except ImportError:
    # Python 2
    from urllib import quote_plus

filter_key = "to_email"
filter_operator = quote_plus("=")
filter_value = "testing@sendgrid.net"
filter_value = quote_plus("\"%s\"" % (filter_value))

params = {}
params["query"] = "%s%s%s" % (filter_key, filter_operator, filter_value)
params["limit"] = 1

response = sg.client.messages.get(query_params=params)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Filter messages by message ID #
# GET /messages/{msg_id} #

msg_id = "test_url_param"
response = sg.client.messages._(msg_id).get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Request a CSV #
# POST /messages/download #

response = sg.client.messages.download.post()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Download CSV #
# GET /messages/download/{download_uuid} #

download_uuid = "test_url_param"
response = sg.client.messages.download._(download_uuid).get()
print(response.status_code)
print(response.body)
print(response.headers)