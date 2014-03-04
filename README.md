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

### Adding Recipients

```python
message = sendgrid.Mail()
message.add_to('example@sendgrid.com')
# or
message.add_to('Example Dude <example@email.com>')
```

### Adding BCC Recipients

```python
message = sendgrid.Mail()
message.add_bcc('example@email.com')
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

### Set File Attachments

```python
message = sendgrid.Mail()
message.add_attachment('./stuff.txt')
# or
message.add_attachment_stream('filename', 'somerandomcontentyouwant')
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

### TODO:

* Add support for CID

### Tests

```bash
python test/__init__.py
```

## MIT License
