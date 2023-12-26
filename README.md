![SendGrid Logo](twilio_sendgrid_logo.png)

[![BuildStatus](https://github.com/sendgrid/sendgrid-python/actions/workflows/test-and-deploy.yml/badge.svg)](https://github.com/sendgrid/sendgrid-python/actions/workflows/test-and-deploy.yml)
[![Docker Badge](https://img.shields.io/docker/automated/sendgrid/sendgrid-python.svg)](https://hub.docker.com/r/sendgrid/sendgrid-python/)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Twitter Follow](https://img.shields.io/twitter/follow/sendgrid.svg?style=social&label=Follow)](https://twitter.com/sendgrid)
[![GitHub contributors](https://img.shields.io/github/contributors/sendgrid/sendgrid-python.svg)](https://github.com/sendgrid/sendgrid-python/graphs/contributors)
[![Open Source Helpers](https://www.codetriage.com/sendgrid/sendgrid-python/badges/users.svg)](https://www.codetriage.com/sendgrid/sendgrid-python)

**This library allows you to quickly and easily use the SendGrid Web API v3 via Python.**

Version 3.X.X+ of this library provides full support for all SendGrid [Web API v3](https://sendgrid.com/docs/API_Reference/Web_API_v3/index.html) endpoints, including the new [v3 /mail/send](https://sendgrid.com/blog/introducing-v3mailsend-sendgrids-new-mail-endpoint).

This library represents the beginning of a new path for SendGrid. We want this library to be community driven and SendGrid led. We need your help to realize this goal. To help make sure we are building the right things in the right order, we ask that you create [issues](https://github.com/sendgrid/sendgrid-python/issues) and [pull requests](CONTRIBUTING.md) or simply upvote or comment on existing issues or pull requests.

**If you need help using SendGrid, please check the [Twilio SendGrid Support Help Center](https://support.sendgrid.com).**

Please browse the rest of this README for further detail.

# Table of Contents

* [Installation](#installation)
* [Quick Start](#quick-start)
* [Processing Inbound Email](#inbound)
* [Usage](#usage)
* [Use Cases](#use-cases)
* [Announcements](#announcements)
* [How to Contribute](#contribute)
* [Troubleshooting](#troubleshooting)
* [About](#about)
* [Support](#support)
* [License](#license)

<a name="installation"></a>

# Installation

## Prerequisites

- Python version 2.7+
- The SendGrid service, starting at the [free level](https://sendgrid.com/free?source=sendgrid-python)

## Setup Environment Variables
### Mac

Update the development environment with your [SENDGRID_API_KEY](https://app.sendgrid.com/settings/api_keys) (more info [here](https://sendgrid.com/docs/User_Guide/Settings/api_keys.html)), for example:

```bash
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
```
SendGrid also supports local environment file `.env`. Copy or rename `.env_sample` into `.env` and update [SENDGRID_API_KEY](https://app.sendgrid.com/settings/api_keys) with your key.

### Windows
Temporarily set the environment variable(accessible only during the current cli session):
```bash
set SENDGRID_API_KEY=YOUR_API_KEY
```
Permanently set the environment variable(accessible in all subsequent cli sessions):
```bash
setx SENDGRID_API_KEY "YOUR_API_KEY"
```

## Install Package
```bash
pip install sendgrid
```

## Dependencies

- [Python-HTTP-Client](https://github.com/sendgrid/python-http-client)
- [ECDSA-Python](https://github.com/starkbank/ecdsa-python)


<a name="quick-start"></a>
# Quick Start

## Hello Email

The following is the minimum needed code to send an email with the [/mail/send Helper](sendgrid/helpers/mail) ([here](examples/helpers/mail_example.py#L9) is a full example):

### With Mail Helper Class

```python
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("test@example.com")
to_email = To("test@example.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
```

The `Mail` constructor creates a [personalization object](https://sendgrid.com/docs/Classroom/Send/v3_Mail_Send/personalizations.html) for you. [Here](examples/helpers/mail_example.py#L28) is an example of how to add it.

### Without Mail Helper Class

The following is the minimum needed code to send an email without the /mail/send Helper ([here](examples/mail/mail.py#L27) is a full example):

```python
import sendgrid
import os

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
data = {
  "personalizations": [
    {
      "to": [
        {
          "email": "test@example.com"
        }
      ],
      "subject": "Sending with SendGrid is Fun"
    }
  ],
  "from": {
    "email": "test@example.com"
  },
  "content": [
    {
      "type": "text/plain",
      "value": "and easy to do anywhere, even with Python"
    }
  ]
}
response = sg.client.mail.send.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)
```

## General v3 Web API Usage (With [Fluent Interface](https://sendgrid.com/blog/using-python-to-implement-a-fluent-interface-to-any-rest-api/))

```python
import sendgrid
import os

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
response = sg.client.suppression.bounces.get()
print(response.status_code)
print(response.body)
print(response.headers)
```

## General v3 Web API Usage (Without Fluent Interface)

```python
import sendgrid
import os

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
response = sg.client._("suppression/bounces").get()
print(response.status_code)
print(response.body)
print(response.headers)
```

<a name="inbound"></a>
# Processing Inbound Email

Please see [our helper](sendgrid/helpers/inbound) for utilizing our Inbound Parse webhook.

<a name="usage"></a>
# Usage

- [SendGrid Documentation](https://sendgrid.com/docs/API_Reference/index.html)
- [Library Usage Documentation](USAGE.md)
- [Example Code](examples)
- [How-to: Migration from v2 to v3](https://sendgrid.com/docs/Classroom/Send/v3_Mail_Send/how_to_migrate_from_v2_to_v3_mail_send.html)
- [v3 Web API Mail Send Helper](sendgrid/helpers/mail) - build a request object payload for a v3 /mail/send API call.
- [Processing Inbound Email](sendgrid/helpers/inbound)

<a name="use-cases"></a>
# Use Cases

[Examples of common API use cases](use_cases/README.md), such as how to send an email with a transactional template.

<a name="announcements"></a>
# Announcements

All updates to this library are documented in our [CHANGELOG](CHANGELOG.md) and [releases](https://github.com/sendgrid/sendgrid-python/releases).

<a name="contribute"></a>
# How to Contribute

We encourage contribution to our libraries (you might even score some nifty swag), please see our [CONTRIBUTING](CONTRIBUTING.md) guide for details.

Quick links:

- [Feature Request](CONTRIBUTING.md#feature-request)
- [Bug Reports](CONTRIBUTING.md#submit-a-bug-report)
- [Improvements to the Codebase](CONTRIBUTING.md#improvements-to-the-codebase)
- [Review Pull Requests](CONTRIBUTING.md#code-reviews)

<a name="troubleshooting"></a>
# Troubleshooting

Please see our [troubleshooting guide](TROUBLESHOOTING.md) for common library issues.

<a name="about"></a>
# About

sendgrid-python is maintained and funded by Twilio SendGrid, Inc. The names and logos for sendgrid-python are trademarks of Twilio SendGrid, Inc.

<a name="support"></a>
# Support

If you need support, please check the [Twilio SendGrid Support Help Center](https://support.sendgrid.com).

<a name="license"></a>
# License
[The MIT License (MIT)](LICENSE)
