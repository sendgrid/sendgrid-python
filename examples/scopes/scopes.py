import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient()

##################################################
# Returns a list of scopes for which this user has access. #
# GET /scopes #

response = sg.client.scopes.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

