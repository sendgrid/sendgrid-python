import sendgrid
import os

from sendgrid import Email, To, Content, Mail

# Example 1
# setting region to be "global"
# sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
sg.set_data_residency("global")
from_email = Email("example@abc.com")
to_email = To("example@abc.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
print(sg.host)
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response)
print(response.status_code)
print(response.body)
print(response.headers)


# Example 2
# setting region to "eu"
sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
sg.set_host("https://api.eu.sendgrid.com")
# sg.set_data_residency("eu")
from_email = Email("example@abc.com")
to_email = To("example@abc.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
print(sg.host)
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response)
print(response.status_code)
print(response.body)
print(response.headers)