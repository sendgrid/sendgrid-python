# Send a Single Email to a Single Recipient

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

```python
import os
import sendgrid
from sendgrid.helpers.mail import *

client = sendgrid.SendGridClientFactory(os.environ.get('SENDGRID_API_KEY'))
from_email = Email("test@example.com", "Example User")
to_email = Email("test@example.com", "Example User")
subject = "Sending with SendGrid is Fun"
plain_text_content = "and easy to do anywhere, even with Python"
html_content = "<strong>and easy to do anywhere, even with Ruby</strong>"
msg = Mail.create_single_email(from_email, subject, to_email, content)
try:
    response = client.send_email(msg)
except urllib.error.HTTPError as e:
    print(e.read())
print(response.status_code)
print(response.body)
print(response.headers)
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
