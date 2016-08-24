[![Travis Badge](https://travis-ci.org/sendgrid/sendgrid-python.svg?branch=master)](https://travis-ci.org/sendgrid/sendgrid-python)

**This library allows you to quickly and easily use the SendGrid Web API v3 via Python.**

Version 3.X.X of this library provides full support for all SendGrid [Web API v3](https://sendgrid.com/docs/API_Reference/Web_API_v3/index.html) endpoints, including the new [v3 /mail/send](https://sendgrid.com/blog/introducing-v3mailsend-sendgrids-new-mail-endpoint).

This library represents the beginning of a new path for SendGrid. We want this library to be community driven and SendGrid led. We need your help to realize this goal. To help make sure we are building the right things in the right order, we ask that you create [issues](https://github.com/sendgrid/sendgrid-python/issues) and [pull requests](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md) or simply upvote or comment on existing issues or pull requests.

Please browse the rest of this README for further detail.

We appreciate your continued support, thank you!

## Table of Contents

* [Installation](#installation)
* [Quick Start](#quick_start)
* [Processing Inbound Email](#inbound)
* [Usage](#usage)
* [Use Cases](#use_cases)
* [Announcements](#announcements)
* [Roadmap](#roadmap)
* [How to Contribute](#contribute)
* [Troubleshooting](#troubleshooting)
* [About](#about)

<a name="installation"></a>
# Installation

## Prerequisites

- Python version 2.6, 2.7, 3.4 or 3.5
- The SendGrid service, starting at the [free level](https://sendgrid.com/free?source=sendgrid-python)

## Setup Environment Variables

Update the development environment with your [SENDGRID_API_KEY](https://app.sendgrid.com/settings/api_keys), for example:

```bash
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
```

## Install Package

```bash
pip install sendgrid
```

## Dependencies

- [Python-HTTP-Client](https://github.com/sendgrid/python-http-client)

<a name="quick_start"></a>
# Quick Start

## Hello Email

The following is the minimum needed code to send an email with the [/mail/send Helper](https://github.com/sendgrid/sendgrid-python/tree/master/sendgrid/helpers/mail) ([here](https://github.com/sendgrid/sendgrid-python/blob/master/examples/helpers/mail/mail_example.py#L20) is a full example):

### With Mail Helper Class

```python
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("test@example.com")
subject = "Hello World from the SendGrid Python Library!"
to_email = Email("test@example.com")
content = Content("text/plain", "Hello, Email!")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
```

The `Mail` constructor creates a [personalization object](https://sendgrid.com/docs/Classroom/Send/v3_Mail_Send/personalizations.html) for you. [Here](https://github.com/sendgrid/sendgrid-python/blob/master/examples/helpers/mail/mail_example.py#L16) is an example of how to add to it.

### Without Mail Helper Class

The following is the minimum needed code to send an email without the /mail/send Helper ([here](https://github.com/sendgrid/sendgrid-python/blob/master/examples/mail/mail.py#L27) is a full example):

```python
import sendgrid
import os

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
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

## General v3 Web API Usage (With Fluent Interface)

```python
import sendgrid
import os

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
response = sg.client.suppression.bounces.get()
print(response.status_code)
print(response.body)
print(response.headers)
```

## General v3 Web API Usage (Without Fluent Interface)

```python
import sendgrid
import os

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
response = sg.client._("suppression/bounces").get()
print(response.status_code)
print(response.body)
print(response.headers)
```

<a name="inbound"></a>
# Processing Inbound Email

Please see [our helper](https://github.com/sendgrid/sendgrid-python/tree/master/sendgrid/helpers/inbound) for utilizing our Inbound Parse webhook.

<a name="usage"></a>
# Usage

- [SendGrid Documentation](https://sendgrid.com/docs/API_Reference/index.html)
- [Library Usage Documentation](https://github.com/sendgrid/sendgrid-python/tree/master/USAGE.md)
- [Example Code](https://github.com/sendgrid/sendgrid-python/tree/master/examples)
- [How-to: Migration from v2 to v3](https://sendgrid.com/docs/Classroom/Send/v3_Mail_Send/how_to_migrate_from_v2_to_v3_mail_send.html)
- [v3 Web API Mail Send Helper](https://github.com/sendgrid/sendgrid-python/tree/master/sendgrid/helpers/mail) - build a request object payload for a v3 /mail/send API call.
- [Processing Inbound Email](https://github.com/sendgrid/sendgrid-python/tree/master/sendgrid/helpers/inbound)

<a name="use_cases">
# Use Cases

[Examples of common API use cases](https://github.com/sendgrid/sendgrid-python/blob/master/USE_CASES.md), such as how to send an email with a transactional template.

<a name="announcements"></a>
# Announcements

All updates to this library is documented in our [CHANGELOG](https://github.com/sendgrid/sendgrid-python/blob/master/CHANGELOG.md) and [releases](https://github.com/sendgrid/sendgrid-python/releases).

<a name="roadmap"></a>
# Roadmap

If you are interested in the future direction of this project, please take a look at our open [issues](https://github.com/sendgrid/sendgrid-python/issues) and [pull requests](https://github.com/sendgrid/sendgrid-python/pulls). We would love to hear your feedback.

<a name="contribute"></a>
# How to Contribute

We encourage contribution to our libraries (you might even score some nifty swag), please see our [CONTRIBUTING](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md) guide for details.

Quick links:

- [Feature Request](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#feature_request)
- [Bug Reports](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#submit_a_bug_report)
- [Sign the CLA to Create a Pull Request](https://github.com/sendgrid/sendgrid-open-source-templates/tree/master/CONTRIBUTING.md#cla)
- [Improvements to the Codebase](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#improvements_to_the_codebase)

<a name="troubleshooting"></a>
# Troubleshooting

Please see our [troubleshooting guide](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md) for common library issues.

<a name="about"></a>
# About

sendgrid-python is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

sendgrid-python is maintained and funded by SendGrid, Inc. The names and logos for sendgrid-python are trademarks of SendGrid, Inc.

![SendGrid Logo]
(https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)
