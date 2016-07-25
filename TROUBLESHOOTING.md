If you have a non-library SendGrid issue, please contact our [support team](https://support.sendgrid.com).

If you can't find a solution below, please open an [issue](https://github.com/sendgrid/sendgrid-python/issues).


## Table of Contents

* [Migrating from v2 to v3](#migrating)
* [Continue Using v2](#v2)
* [Testing v3 /mail/send Calls Directly](#testing)
* [Error Messages](#error)
* [Versions](#versions)
* [Environment Variables and Your SendGrid API Key](#environment)
* [Using the Package Manager](#package-manager)

<a name="migrating"></a>
## Migrating from v2 to v3

Please review [our guide](https://sendgrid.com/docs/Classroom/Send/v3_Mail_Send/how_to_migrate_from_v2_to_v3_mail_send.html) on how to migrate from v2 to v3.

<a name="v2"></a>
## Continue Using v2

[Here](https://github.com/sendgrid/sendgrid-python/tree/0942f9de2d5ba5fedb65a23940ebe1005a21a6c7) is the last working version with v2 support.

Using pip:

```bash
pip unistall sendgrid
pip install sendgrid=1.6.22
```

Download:

Click the "Clone or download" green button in [GitHub](https://github.com/sendgrid/sendgrid-python/tree/0942f9de2d5ba5fedb65a23940ebe1005a21a6c7) and choose download.

<a name="testing"></a>
## Testing v3 /mail/send Calls Directly

[Here](https://sendgrid.com/docs/Classroom/Send/v3_Mail_Send/curl_examples.html) are some cURL examples for common use cases.

<a name="error"></a>
## Error Messages

To read the error message returned by SendGrid's API:

```python
try:
  response = sg.client.mail.send.post(request_body=mail.get())
except urllib2.HTTPError as e:
    print e.read()
```

<a name="versions"></a>
## Versions

We follow the MAJOR.MINOR.PATCH versioning scheme as described by [SemVer.org](http://semver.org). Therefore, we recommend that you always pin (or vendor) the particular version you are working with to your code and never auto-update to the latest version. Especially when there is a MAJOR point release, since that is guarenteed to be a breaking change.

<a name="environment"></a>
## Environment Variables and Your SendGrid API Key

All of our examples assume you are using [environment variables](https://github.com/sendgrid/sendgrid-python#setup-environment-variables) to hold your SendGrid API key.

If you choose to add your SendGrid API key directly (not recommended):

`apikey=os.environ.get('SENDGRID_API_KEY')`

becomes

`apikey='SENDGRID_API_KEY'`

In the first case SENDGRID_API_KEY is in reference to the name of the environment variable, while the second case references the actual SendGrid API Key.

<a name="package-manager"></a>
## Using the Package Manager

We upload this library to [PyPI](https://pypi.python.org/pypi/sendgrid) whenever we make a release. This allows you to use [pip](https://pypi.python.org/pypi/pip) for easy installation.

In most cases we recommend you download the latest version of the library, but if you need a different version, please use:

`pip install sendgrid==X.X.X`

If you are usring a [requirements file](https://pip.readthedocs.io/en/1.1/requirements.html), please use:

`sendgrid==X.X.X`