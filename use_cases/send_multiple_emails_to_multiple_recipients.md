```python
import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To

to_emails = [
    To(email='test+to0@example.com',
       name='Example Name 0',
       substitutions={
           '-name-': 'Example Name Substitution 0',
           '-github-': 'https://example.com/test0',
       },
       subject='Override Global Subject'),
    To(email='test+to1@example.com',
       name='Example Name 1',
       substitutions={
           '-name-': 'Example Name Substitution 1',
           '-github-': 'https://example.com/test1',
       }),
]
global_substitutions = {'-time-': '2019-01-01 00:00:00'}
message = Mail(
    from_email=('test+from@example.com', 'Example From Name'),
    to_emails=to_emails,
    subject='Hi -name-, this is the global subject',
    html_content='<strong>Hello -name-, your URL is ' +
    '<a href=\"-github-\">here</a></strong> email sent at -time-',
    global_substitutions=global_substitutions,
    is_multiple=True)
try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
```