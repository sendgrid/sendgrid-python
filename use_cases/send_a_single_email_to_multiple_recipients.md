```python
import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

to_emails = [
    ('test0@example.com', 'Example Name 0'),
    ('test1@example.com', 'Example Name 1')
]
message = Mail(
    from_email=('from@example.com', 'Example From Name'),
    to_emails=to_emails,
    subject='Sending with SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
```