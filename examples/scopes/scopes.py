import sendgrid
import os


sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

##################################################
# Retrieve a list of scopes for which this user has access. #
# GET /scopes #

response = sg.client.scopes.get()
print(response.status_code)
print(response.body)
print(response.headers)
