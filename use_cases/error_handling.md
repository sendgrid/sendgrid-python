# Error Handling
[Custom exceptions](https://github.com/sendgrid/python-http-client/blob/master/python_http_client/exceptions.py) for `python_http_client` are now supported, which can be imported by consuming libraries.

Please see [here](https://github.com/sendgrid/python-http-client/blob/master/python_http_client/exceptions.py) for a list of supported exceptions.

```python
  import sendgrid
  import os
  from sendgrid.helpers.mail import *
  from python_http_client import exceptions

  sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
  from_email = Email("dx@sendgrid.com")
  to_email = Email("elmer.thomas@sendgrid.com")
  subject = "Sending with SendGrid is Fun"
  content = Content("text/plain", "and easy to do anywhere, even with Python")
  mail = Mail(from_email, subject, to_email, content)
  try:
      response = sg.client.mail.send.post(request_body=mail.get())
  except exceptions.BadRequestsError as e:
      print(e.body)
      exit()
  print(response.status_code)
  print(response.body)
  print(response.headers)
```