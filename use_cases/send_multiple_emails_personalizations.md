```python
import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Personalization, From, To, Cc, Bcc

# Note that the domain for all From email addresses must match
message = Mail(
    from_email=('from@example.com', 'Example From Name'),
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

personalization1 = Personalization()
personalization1.add_email(To('test0@example.com', 'Example Name 0'))
personalization1.add_email(Cc('test1@example.com', 'Example Name 1'))
message.add_personalization(personalization1)

personalization2 = Personalization()
personalization2.add_email(To('test2@example.com', 'Example Name 2'))
personalization2.add_email(Bcc('test3@example.com', 'Example Name 3'))
personalization2.add_email(From('from2@example.com', 'Example From Name 2'))
message.add_personalization(personalization2)

try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
```