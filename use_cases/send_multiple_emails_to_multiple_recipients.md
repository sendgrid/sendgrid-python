```python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To

to_emails = [
    To(email='test+to0@example.com',
       name='Example Name 0',
       dynamic_template_data={
           'name': 'Dynamic Name 0',
           'url': 'https://example.com/test0',
       },
       subject='Override Global Subject'),
    To(email='test+to1@example.com',
       name='Example Name 1',
       dynamic_template_data={
           'name': 'Dynamic Name 1',
           'url': 'https://example.com/test1',
       }),
]
message = Mail(
    from_email=('test+from@example.com', 'Example From Name'),
    to_emails=to_emails,
    subject='Global subject',
    is_multiple=True)
message.template_id = 'd-12345678901234567890123456789012'

try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
```
