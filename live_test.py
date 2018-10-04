# Send a Single Email to a Single Recipient
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, SendGridException

message = Mail(from_email=From('dx@sendgrid.com', 'DX'),
               to_emails=To('elmer.thomas@sendgrid.com', 'Elmer Thomas'),
               subject=Subject('Sending with SendGrid is Fun'),
               plain_text_content=PlainTextContent('and easy to do anywhere, even with Python'),
               html_content=HtmlContent('<strong>and easy to do anywhere, even with Python</strong>'))

try:
    sendgrid_client = SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message=message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except SendGridException as e:
    print(e.message)

# ToDo

## The Mail constructor should also support passing in tuples and strings
## The send function parameter should be better named, maybe email_message or simply message
