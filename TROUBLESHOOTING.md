If you have an issue logging into your Twilio SendGrid account, please read this [document](https://sendgrid.com/docs/ui/account-and-settings/troubleshooting-login/). For any questions regarding login issues, please contact our [support team](https://support.sendgrid.com).

If you have a non-library Twilio SendGrid issue, please contact our [support team](https://support.sendgrid.com).

If you can't find a solution below, please open an [issue](https://github.com/sendgrid/sendgrid-python/issues).

## Table of Contents

* [Environment Variables and Your Twilio SendGrid API Key](#environment)
* [Error Messages](#error)
* [Migrating from v2 to v3](#migrating)
* [Continue Using v2](#v2)
* [Testing v3 /mail/send Calls Directly](#testing)
* [Using the Package Manager](#package-manager)
* [Version Convention](#versions)
* [Viewing the Request Body](#request-body)
* [Error Handling](#error-handling)

<a name="environment"></a>
## Environment Variables and Your Twilio SendGrid API Key

All of our examples assume you are using [environment variables](https://github.com/sendgrid/sendgrid-python#setup-environment-variables) to hold your Twilio SendGrid API key.

If you choose to add your Twilio SendGrid API key directly (not recommended):

`api_key=os.environ.get('SENDGRID_API_KEY')`

becomes

`api_key='SENDGRID_API_KEY'`

In the first case, SENDGRID_API_KEY is in reference to the name of the environment variable, while the second case references the actual Twilio SendGrid API Key.

<a name="error"></a>
## Error Messages

HTTP exceptions are defined in the [`python_http_client` package](https://github.com/sendgrid/python-http-client/blob/HEAD/python_http_client/exceptions.py).

To read the error message returned by SendGrid's API in Python 2.X:

```python
from python_http_client.exceptions import HTTPError

try:
  response = sg.client.mail.send.post(request_body=mail.get())
except HTTPError as e:
    print e.to_dict
```

To read the error message returned by Twilio SendGrid's API in Python 3.X:

```python
from python_http_client.exceptions import HTTPError

try:
  response = sg.client.mail.send.post(request_body=mail.get())
except HTTPError as e:
    print(e.to_dict)
```

<a name="migrating"></a>
## Migrating from v2 to v3

Please review [our guide](https://sendgrid.com/docs/Classroom/Send/v3_Mail_Send/how_to_migrate_from_v2_to_v3_mail_send.html) on how to migrate from v2 to v3.

<a name="v2"></a>
## Continue Using v2

[Here](https://github.com/sendgrid/sendgrid-python/tree/0942f9de2d5ba5fedb65a23940ebe1005a21a6c7) is the last working version with v2 support.

Using pip:

```bash
pip uninstall sendgrid
pip install sendgrid==1.6.22
```

Download:

Click the "Clone or download" green button in [GitHub](https://github.com/sendgrid/sendgrid-python/tree/0942f9de2d5ba5fedb65a23940ebe1005a21a6c7) and choose download.

<a name="testing"></a>
## Testing v3 /mail/send Calls Directly

[Here](https://sendgrid.com/docs/for-developers/sending-email/curl-examples) are some cURL examples for common use cases.

<a name="package-manager"></a>
## Using the Package Manager

We upload this library to [PyPI](https://pypi.python.org/pypi/sendgrid) whenever we make a release. This allows you to use [pip](https://pypi.python.org/pypi/pip) for easy installation.

In most cases we recommend you download the latest version of the library, but if you need a different version, please use:

`pip install sendgrid==X.X.X`

If you are using a [requirements file](https://pip.readthedocs.io/en/1.1/requirements.html), please use:

`sendgrid==X.X.X`

<a name="versions"></a>
## Versioning Convention

We follow the MAJOR.MINOR.PATCH versioning scheme as described by [SemVer.org](http://semver.org). Therefore, we recommend that you always pin (or vendor) the particular version you are working with to your code and never auto-update to the latest version. Especially when there is a MAJOR point release, since that is guaranteed to be a breaking change. Changes are documented in the [CHANGELOG](CHANGELOG.md) and [releases](https://github.com/sendgrid/sendgrid-python/releases) section.

<a name="request-body"></a>
## Viewing the Request Body

When debugging or testing, it may be useful to examine the raw request body to compare against the [documented format](https://sendgrid.com/docs/API_Reference/api_v3.html).

You can do this right before you call `response = sg.client.mail.send.post(request_body=mail.get())` like so:

```python
 print(json.dumps(message.get(), sort_keys=True, indent=4))
```

<a name="error-handling"></a>
# Error Handling

Please review [our use_cases](use_cases/README.md) for examples of error handling.
