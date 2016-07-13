[![Travis Badge](https://travis-ci.org/sendgrid/sendgrid-python.svg?branch=master)](https://travis-ci.org/sendgrid/sendgrid-python)

**This library allows you to quickly and easily use the SendGrid Web API via Python.**

# Announcements

**BREAKING CHANGE as of 2016.06.14**

Version 3.X.X is a breaking change for the entire library. Generally, any [major point release](http://semver.org/) will be a breaking change.

Version 3.X.X brings you full support for all Web API v3 endpoints. We
have the following resources to get you started quickly:

-   [General Documentation](https://sendgrid.com/docs/API_Reference/Web_API_v3/index.html)
-   [Python Usage
    Documentation](https://github.com/sendgrid/sendgrid-python/tree/master/USAGE.md)
-   [Python Example
    Code](https://github.com/sendgrid/sendgrid-python/tree/master/examples)
-   [How-to: Migration from v2 to v3](https://sendgrid.com/docs/Classroom/Send/v3_Mail_Send/how_to_migrate_from_v2_to_v3_mail_send.html)

This is the first of many iterations and we need your help to determine priority. You can help by creating [issues](https://github.com/sendgrid/sendgrid-python/issues), [pull requests](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md) or simply upvoting or commenting on existing issues or pull requests.

We appreciate your continued support, thank you!

All updates to this library is documented in our [CHANGELOG](https://github.com/sendgrid/sendgrid-python/blob/master/CHANGELOG.md).

# Installation

## Setup Environment Variables

First, get your free SendGrid account [here](https://sendgrid.com/free?source=sendgrid-python).

Next, update your environment with your [SENDGRID_API_KEY](https://app.sendgrid.com/settings/api_keys).

```bash
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
```

## Install Package

```bash
pip install sendgrid
```

or

```bash
easy_install sendgrid
```

## Dependencies

- The SendGrid Service, starting at the [free level](https://sendgrid.com/free?source=sendgrid-python)
- [Python-HTTP-Client](https://github.com/sendgrid/python-http-client)

# Quick Start

## Hello Email

The minimum needed code to send an email with the [/mail/send Helper](https://github.com/sendgrid/sendgrid-python/tree/master/sendgrid/helpers/mail) ([here]() is a full example):

```python
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("test@example.com")
subject = "Hello World from the SendGrid Python Library!"
to_email = Email("test@example.com")
content = Content("text/plain", "Hello, Email!")
# The constructor creates a personalization object for you, to add to it,
# please see [this example](https://github.com/sendgrid/sendgrid-python/blob/master/examples/helpers/mail/mail_example.py#L16).
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
```

The minimum needed code to send an email without the /mail/send Helper ([here]() is a full example):

```python
import sendgrid
import os

data = {
  "personalizations": [
    {
      "to": [
        {
          "email": "test@example.com"
        }
      ],
      "subject": "Hello World from the SendGrid Python Library!"
    }
  ],
  "from": {
    "email": "test@example.com"
  },
  "content": [
    {
      "type": "text/plain",
      "value": "Hello, Email!"
    }
  ]
}
response = sg.client.mail.send.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)
```

## General v3 Web API Usage

```python
import sendgrid
import os

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
response = sg.client.api_keys.get()
print(response.status_code)
print(response.body)
print(response.headers)
```

# Usage

- [SendGrid Documentation](https://sendgrid.com/docs/API_Reference/index.html)
- [Usage Documentation](https://github.com/sendgrid/sendgrid-python/tree/master/USAGE.md)
- [Example Code](https://github.com/sendgrid/sendgrid-python/tree/master/examples)
- [v3 Web API Mail Send Helper](https://github.com/sendgrid/sendgrid-python/tree/master/sendgrid/helpers/mail) - build a request object payload for a v3 /mail/send API call.

## Roadmap

If you are intersted in the future direction of this project, please take a look at our [milestones](https://github.com/sendgrid/sendgrid-python/milestones). We would love to hear your feedback.

## How to Contribute

We encourage contribution to our libraries, please see our [CONTRIBUTING](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md) guide for details.

Quick links:

- [Feature Request](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#feature_request)
- [Bug Reports](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#submit_a_bug_report)
- [Sign the CLA to Create a Pull Request](https://github.com/sendgrid/sendgrid-open-source-templates/tree/master/CONTRIBUTING.md#cla)
- [Improvements to the Codebase](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#improvements_to_the_codebase)

# About

sendgrid-python is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

sendgrid-python is maintained and funded by SendGrid, Inc. The names and logos for sendgrid-python are trademarks of SendGrid, Inc.

![SendGrid Logo]
(https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)
