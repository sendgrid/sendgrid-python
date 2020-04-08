# Error Handling
[Custom exceptions](https://github.com/sendgrid/python-http-client/blob/master/python_http_client/exceptions.py) for `python_http_client` are now supported.

Please see [here](https://github.com/sendgrid/python-http-client/blob/master/python_http_client/exceptions.py) for a list of supported exceptions.

There are also email specific exceptions located [here](https://github.com/sendgrid/sendgrid-python/blob/master/sendgrid/helpers/mail/exceptions.py)

```python
  import os
  from sendgrid import SendGridAPIClient
  from sendgrid.helpers.mail import (From, To, Subject, PlainTextContent, HtmlContent, Mail)
  from python_http_client import exceptions

  sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
  from_email = From("help@twilio.com")
  to_email = To("ethomas@twilio.com")
  subject = Subject("Sending with Twilio SendGrid is Fun")
  plain_text_content = PlainTextContent("and easy to do anywhere, even with Python")
  html_content = HtmlContent("<strong>and easy to do anywhere, even with Python</strong>")
  message = Mail(from_email, to_email, subject, plain_text_content, html_content)
  try:
      response = sendgrid_client.send(message)
      print(response.status_code)
      print(response.body)
      print(response.headers)
  except exceptions.BadRequestsError as e:
      print(e.body)
      exit()
```
