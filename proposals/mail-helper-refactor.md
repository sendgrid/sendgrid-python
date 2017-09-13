# Send a Single Email to a Single Recipient

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

This is the minimum code needed to send an email.

```python
import os
import sendgrid
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent

msg = Mail(from_email=From('from@example.com', 'From Name'),
           to_email=To('to@example.com', 'To Name'),
           subject=Subject('Sending with SendGrid is Fun'),
           plain_text_content=PlainTextContent('and easy to do anywhere, even with Python'),
           html_content=HtmlContent('<strong>and easy to do anywhere, even with Ruby</strong>'))

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

```python
import os
import sendgrid
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent

to_emails = [
    To('to0@example.com', 'To Name 0'),
    To('to1@example.com', 'To Name 1')
]
msg = Mail(from_email=From('from@example.com', 'From Name'),
           to_emails=tos,
           subject=Subject('Sending with SendGrid is Fun'),
           plain_text_content=PlainTextContent('and easy to do anywhere, even with Python'),
           html_content=HtmlContent('<strong>and easy to do anywhere, even with Ruby</strong>'))

try:
    response = sendgrid.send(msg, api_key=os.environ.get('SENDGRID_API_KEY'))
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.read())
```

# Send Multiple Emails to Multiple Recipients

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

```python
import os
import sendgrid
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent

to_emails = [
    To(email='to0@example.com',
       name='To Name 0',
       substitutions={
           '-name-': 'To Name 0',
           '-github-': 'http://github.com/mbernier',
       },
       subject=Subject('Override Global Subject')),
    To(email='to1@example.com',
       name='To Name 1',
       substitutions={
           '-name-': 'To Name 1',
           '-github-': 'http://github.com/thinkingserious',
       })
]
from time import gmtime, strftime
global_substitutions = {
    '-time-': strftime("%Y-%m-%d %H:%M:%S", gmtime())
}
msg = Mail(from_email=From('from@example.com', 'From Name'),
           to_emails=tos,
           subject=Subject('Hi -name-'),
           plain_text_content=PlainTextContent('Hello -name-, your github is -github-, email sent at -time-'),
           html_content=HtmlContent('<strong>Hello -name-, your github is <a href=\"-github-\">here</a></strong> email sent at -time-'),
           global_substitutions=global_substitutions)

try:
    response = sendgrid.send(msg, api_key=os.environ.get('SENDGRID_API_KEY'))
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.read())
```

# Kitchen Sink - an example with all settings used

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

Coming soon

# Attachments

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

Coming soon

# Transactional Templates

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

Coming soon
