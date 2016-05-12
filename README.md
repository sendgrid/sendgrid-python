# Special Announcement

We have released a [v3 beta branch](https://github.com/sendgrid/sendgrid-python/tree/v3beta) for this library that supports our new v3 Mail Send endpoint which is in open beta. The v3/mail/send/beta endpoint is not a production endpoint, so you should not integrate with it for your production email sending. However, when we make this an officially released feature it will be available at v3/mail//send.

Please try it out and let us know what you think about the endpoint and the library in the [issues area of this repo](https://github.com/sendgrid/sendgrid-python/issues]), all of your feedback will be taken into account to influence the endpoint and this library.

Beginning with v3/mail/send/beta, the new version of our library will only support v3 endpoints.. Once this endpoint is out of beta, we will update the endpoint, removing the “/beta” from the URI. At this point, the v3 beta branch will be merged to master and will be our official library going forward. This means that we will no longer formally support the v2 mail.send.json endpoint in any of our libraries.

So long as you are not automatically pulling new versions of the library into your production code base, your integration will not break regardless of which endpoint you’re using. By the way, don't pull new versions into your production code base, because breaking changes break things.

The /api/mail.send.json endpoint, known as v2 mail send, is NOT going away. It will continue to work as it always has, happily sending your emails along as if nothing happened.

[![Travis Badge](https://travis-ci.org/sendgrid/sendgrid-python.svg?branch=master)](https://travis-ci.org/sendgrid/sendgrid-python)

**This library allows you to quickly and easily use the SendGrid Web API via Python.**

Currently this library supports our [v2 Mail endpoint](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) and the [v3 Web API](https://sendgrid.com/docs/API_Reference/Web_API_v3/index.html).

# Installation

`pip install sendgrid`

or

`easy_install sendgrid`

## Dependencies

- The SendGrid Service, starting at the [free level](https://sendgrid.com/free?source=sendgrid-python)
- [SMTAPI-Python](https://github.com/sendgrid/smtpapi-python)
- [Python-HTTP-Client](https://github.com/sendgrid/python-http-client)

## Environment Variables (for v3 Web API)

[Sample .env](https://github.com/sendgrid/sendgrid-python/blob/master/.env_sample), please rename to `.env` and add your [SendGrid API Key](https://app.sendgrid.com/settings/api_keys), or you can pass your API Key into the SendGridClient constructor.

# Quick Start

## v2 Mail Send endpoint (Send an Email)

```python
import sendgrid

sg = sendgrid.SendGridClient('YOUR_SENDGRID_API_KEY')


message = sendgrid.Mail()
message.add_to('John Doe <john@email.com>')
message.set_subject('Example')
message.set_html('Body')
message.set_text('Body')
message.set_from('Doe John <doe@email.com>')
status, msg = sg.send(message)
print(status, msg)

#or

message = sendgrid.Mail(to='john@email.com', subject='Example', html='Body', text='Body', from_email='doe@email.com')
status, msg = sg.send(message)
print(status, msg)
```

## v3 Web API endpoints

```python
import sendgrid

sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

response = sg.client.api_keys.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)
```

# Announcements

**BREAKING CHANGE as of 2016.03.01**

Version `2.0.0` is a breaking change for the **Web API v3 endpoints**. The
mail send endpoint is not affected by this update.

Version 2.0.0 brings you full support for all Web API v3 endpoints. We
have the following resources to get you started quickly:

-   [SendGrid
    Documentation](https://sendgrid.com/docs/API_Reference/Web_API_v3/index.html)
-   [Usage
    Documentation](https://github.com/sendgrid/sendgrid-python/blob/master/USAGE.md)
-   [Example
    Code](https://github.com/sendgrid/sendgrid-python/blob/master/examples)

Thank you for your continued support!

For the **v2 Mail Send Endpoint**, if you upgrade to version `1.2.x`, the `add_to` method behaves
differently. In the past this method defaulted to using the `SMTPAPI`
header. Now you must explicitly call the `smtpapi.add_to` method. More
on the `SMTPAPI` section.

## Roadmap

[Milestones](https://github.com/sendgrid/sendgrid-python/milestones)

## How to Contribute

We encourage contribution to our libraries, please see our [CONTRIBUTING](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md) guide for details.

* [Feature Request](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#feature_request)
* [Bug Reports](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#submit_a_bug_report)
* [Improvements to the Codebase](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#improvements_to_the_codebase)

## Usage

- [SendGrid Docs](https://sendgrid.com/docs/API_Reference/index.html)
- [v2 Mail Send](https://github.com/sendgrid/sendgrid-python/blob/master/USAGE_v2.md)
- [v3 Web API](https://github.com/sendgrid/sendgrid-python/blob/master/USAGE.md)
- [Example Code](https://github.com/sendgrid/sendgrid-python/blob/master/examples)

## Unsupported Libraries

- [Official and Unsupported SendGrid Libraries](https://sendgrid.com/docs/Integrate/libraries.html)

# About

![SendGrid Logo]
(https://assets3.sendgrid.com/mkt/assets/logos_brands/small/sglogo_2015_blue-9c87423c2ff2ff393ebce1ab3bd018a4.png)

sendgrid-python is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

sendgrid-python is maintained and funded by SendGrid, Inc. The names and logos for sendgrid-python are trademarks of SendGrid, Inc.
