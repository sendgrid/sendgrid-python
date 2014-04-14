# SendGrid-Python #
This library allows you to quickly and easily send emails through SendGrid using Python.

[![Build Status](https://travis-ci.org/sendgrid/sendgrid-python.png?branch=master)](https://travis-ci.org/sendgrid/sendgrid-python)

**Warning!** This library was recently updated to bring it up to date with all of our other libraries. It behaves completely different from the previous release. Also, SMTP has been deprecated in support for the Web API.

## Install

```bash
pip install sendgrid
# or
easy_install sendgrid
```

## Example

```python
import sendgrid

sg = sendgrid.SendGridClient('YOUR_SENDGRID_USERNAME', 'YOUR_SENDGRID_PASSWORD')

message = sendgrid.Mail()
message.add_to('John Doe <john@email.com>')
message.set_subject('Example')
message.set_html('Body')
message.set_text('Body')
message.set_from('Doe John <doe@email.com>')
status, msg = sg.send(message)

#or

message = sendgrid.Mail(to='john@email.com', subject='Example', html='Body', text='Body', from_email='doe@email.com')
status, msg = sg.send(message)

```

### Error handling

By default, `.send` method returns a tuple `(http_status_code, message)`,
however you can pass `raise_errors=True` to `SendGridClient` constructor,
then `.send` method will raise `SendGridClientError` for 4xx errors,
and `SendGridServerError` for 5xx errors.

```python
from sendgrid import SendGridError, SendGridClientError, SendGridServerError

sg = sendgrid.SendGridClient(username, password, raise_errors=True)

try:
    sg.send(message)
except SendGridClientError:
    ...
except SendGridServerError:
    ...
```

This behavior is going to be default from version 1.0.0. You are
encouraged to set `raise_errors` to `True` for forwards compatibility.

`SendGridError` is a base-class for all SendGrid-related exceptions.


### Adding Recipients

```python
message = sendgrid.Mail()
message.add_to('example@sendgrid.com')
# or
message.add_to('Example Dude <example@email.com>')
# or
message.add_to(['Example Dude <example@email.com>', 'john@email.com'])
```

### Adding BCC Recipients

```python
message = sendgrid.Mail()
message.add_bcc('example@email.com')
# or
message.add_bcc(['Example Dude <example@email.com>', 'john@email.com'])
```

### Setting the Subject

```python
message = sendgrid.Mail()
message.set_subject('Example')
```

### Set Text or HTML

```python
message = sendgrid.Mail()
message.set_text('Body')
# or
message.set_html('<html><body>Stuff, you know?</body></html>')
```

### Set From

```python
message = sendgrid.Mail()
message.set_from('example@email.com')
```

### Set ReplyTo

```python
message = sendgrid.Mail()
message.set_replyto('example@email.com')
```

### Set File Attachments

```python
message = sendgrid.Mail()
message.add_attachment('stuff.txt', './stuff.txt')
# or
message.add_attachment_stream('filename', 'somerandomcontentyouwant')
# strings, unicode, or BytesIO streams
```

## SendGrid's  [X-SMTPAPI](http://sendgrid.com/docs/API_Reference/SMTP_API/)

If you wish to use the X-SMTPAPI on your own app, you can use the [SMTPAPI Python library](https://github.com/sendgrid/smtpapi-python).

There are implementations for setter methods too.

### [Substitution](http://sendgrid.com/docs/API_Reference/SMTP_API/substitution_tags.html)

```python
message = sendgrid.Mail()
message.add_substitution("key", "value")
```

### [Section](http://sendgrid.com/docs/API_Reference/SMTP_API/section_tags.html)

```python
message = sendgrid.Mail()
message.add_section("section", "value")
```

### [Category](http://sendgrid.com/docs/Delivery_Metrics/categories.html)

```python
message = sendgrid.Mail()
message.add_category("category")
```

### [Unique Arguments](http://sendgrid.com/docs/API_Reference/SMTP_API/unique_arguments.html)

```python
message = sendgrid.Mail()
message.add_unique_arg("key", "value")
```

### [Filter](http://sendgrid.com/docs/API_Reference/SMTP_API/apps.html)

```python
message = sendgrid.Mail()
message.add_filter("filter", "setting", "value")
```

## SMTP

SMTP support has been deprecated from all of our libs. But for those whom still want to use it, here is an example:

```python
import smtplib
from email.mime.text import MIMEText

email = MIMEText("this is a text/plain email") # you can make this html too.

email['Subject'] = 'This will be the subject'
email['From'] = 'yamil@sendgrid.com'
email['To'] = 'example@email.com'
email['Cc'] = 'yamil.asusta@sendgrid.com, jose@sendgrid.com' # this is comma separated field

s = smtplib.SMTP('smtp.sendgrid.net', 587)
s.login('SENDGRID_USER', 'SENDGRID_PASSWORD')
s.sendmail(email['From'], [email['To']], email.as_string())
```

### TODO:

* Add support for CID

### Tests

```bash
python test/__init__.py
```

## MIT License
