[![Travis Badge](https://travis-ci.org/sendgrid/sendgrid-python.svg?branch=master)](https://travis-ci.org/sendgrid/sendgrid-python)

**This library allows you to quickly and easily use the SendGrid Web API via Python.**

# Installation

`pip install sendgrid`

or

`easy_install sendgrid`

## Dependencies

- The SendGrid Service, starting at the [free level](https://sendgrid.com/free?source=sendgrid-python)
- [Python-HTTP-Client](https://github.com/sendgrid/python-http-client)

## Environment Variables

First, get your free SendGrid account [here](https://sendgrid.com/free?source=sendgrid-python).

Next, update your environment with your [SENDGRID_API_KEY](https://app.sendgrid.com/settings/api_keys).

```bash
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
```

# Quick Start

## Hello Email

```python
import sendgrid
from sendgrid.helpers.mail import *

from_email = Email("dx@sendgrid.com")
subject = "Hello World from the SendGrid Python Library"
to_email = Email("elmer.thomas@sendgrid.com")
content = Content("text/plain", "some text here")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.beta.post(request_body=mail.get())
print(response.status_code)
print(response.response_body)
print(response.response_headers)
```

## General v3 Web API Usage

```python
import sendgrid

sg = sendgrid.SendGridAPIClient()
response = sg.client.api_keys.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)
```

# Usage

- [SendGrid Docs](https://sendgrid.com/docs/API_Reference/index.html)
- [v3 Web API](https://github.com/sendgrid/sendgrid-python/blob/master/USAGE.md)
- [Example Code](https://github.com/sendgrid/sendgrid-python/blob/master/examples)
- [v3 Web API Mail Send Helper]()

# Announcements

**BREAKING CHANGE as of XXXX.XX.XX**

Version 3.0.0 brings you full support for all Web API v3 endpoints. We
have the following resources to get you started quickly:

-   [SendGrid
    Documentation](https://sendgrid.com/docs/API_Reference/Web_API_v3/index.html)
-   [Usage
    Documentation](https://github.com/sendgrid/sendgrid-python/blob/master/USAGE.md)
-   [Example
    Code](https://github.com/sendgrid/sendgrid-python/blob/master/examples)

Thank you for your continued support!

## Roadmap

[Milestones](https://github.com/sendgrid/sendgrid-python/milestones)

## How to Contribute

We encourage contribution to our libraries, please see our [CONTRIBUTING](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md) guide for details.

* [Feature Request](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#feature_request)
* [Bug Reports](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#submit_a_bug_report)
* [Improvements to the Codebase](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#improvements_to_the_codebase)

## Unsupported Libraries

- [Official and Unsupported SendGrid Libraries](https://sendgrid.com/docs/Integrate/libraries.html)

# About

![SendGrid Logo]
(https://assets3.sendgrid.com/mkt/assets/logos_brands/small/sglogo_2015_blue-9c87423c2ff2ff393ebce1ab3bd018a4.png)

sendgrid-python is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

sendgrid-python is maintained and funded by SendGrid, Inc. The names and logos for sendgrid-python are trademarks of SendGrid, Inc.
