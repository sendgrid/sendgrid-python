# Send a Single Email to a Single Recipient

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

```python
import os
import sendgrid
from sendgrid.helpers.mail import From, To, Subject, PlainTextContent, HtmlContent, Mail

msg = Mail(From("test@example.com", "Example User"),
           To("test@example.com", "Example User"),
           Subject("Sending with SendGrid is Fun"),
           PlainTextContent("and easy to do anywhere, even with Python"),
           HtmlContent("<strong>and easy to do anywhere, even with Ruby</strong>"))

try:
    response = sendgrid.send(msg, api_key=os.environ.get('SENDGRID_API_KEY'))
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.read())
```

# Send a Single Email to Multiple Recipients

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

Coming soon

# Send Multiple Emails to Multiple Recipients

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

Coming soon

# Attachments

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

Coming soon

# Transactional Templates

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

Coming soon
