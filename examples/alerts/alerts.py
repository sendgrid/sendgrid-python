import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

##################################################
# Create a new Alert #
# POST /alerts #

data = {
    "email_to": "example@example.com",
    "frequency": "daily",
    "type": "stats_notification"
}
response = sg.client.alerts.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve all alerts #
# GET /alerts #

response = sg.client.alerts.get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Update an alert #
# PATCH /alerts/{alert_id} #

data = {
    "email_to": "example@example.com"
}
alert_id = "test_url_param"
response = sg.client.alerts._(alert_id).patch(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Retrieve a specific alert #
# GET /alerts/{alert_id} #

alert_id = "test_url_param"
response = sg.client.alerts._(alert_id).get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Delete an alert #
# DELETE /alerts/{alert_id} #

alert_id = "test_url_param"
response = sg.client.alerts._(alert_id).delete()
print(response.status_code)
print(response.body)
print(response.headers)
