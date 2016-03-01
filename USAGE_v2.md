# INITIALIZATION
To begin using this library create a new instance of SendGridClient with
your SendGrid API Key. To configure API keys, visit
<https://app.sendgrid.com/settings/api_keys>.

```python
sg = sendgrid.SendGridClient('YOUR_SENDGRID_API_KEY')
```

# Table of Contents

* [v2 MAIL SEND METHODS](#methods)
* [SET FILE ATTACHEMENTS](#set_file_attachments)
* [SMTPAPI](#smtpapi)
* [USING TEMPLATES FROM THE TEMPLATE ENGINE](#template_engine)
* [ERROR HANDLING](#error_handling)

<a name="methods"></a>
# METHODS

There are multiple ways to add recipients:

## add\_to

```python
message = sendgrid.Mail()
message.add_to('example@email.com')
# or
message.add_to('Example Dude <example@email.com>')
# or
message.add_to(['Example Dude <example@email.com>', 'john@email.com'])
```

## add\_to\_name

```python
message = sendgrid.Mail()
message.add_to('example@email.com')
message.add_to_name('Example Dude')
```

## add\_cc

```python
message = sendgrid.Mail()
message.add_cc('example@email.com')
message.add_cc(['example@email.com', 'john@email.com'])
```

## add\_bcc

```python
message = sendgrid.Mail()
message.add_bcc('example@email.com')
# or
message.add_bcc(['Example Dude <example@email.com>', 'john@email.com'])
```

## set\_from

```python
message = sendgrid.Mail()
message.set_from('example@email.com')
```

## set\_from\_name

```python
message = sendgrid.Mail()
message.set_from('example@email.com')
message.set_from_name('Example Dude')
```

## set\_replyto

```python
message.sendgrid.Mail()
message.set_replyto('example@email.com')
```

## set\_subject

```python
message = sendgrid.Mail()
message.set_subject('Example')
```

## set\_text

```python
message = sendgrid.Mail()
message.set_text('Body')
```

## set\_html

```python
message = sendgrid.Mail()
message.set_html('<html><body>Stuff, you know?</body></html>')
```

## set\_date

```python
message = sendgrid.Mail()
message.set_date('Wed, 17 Dec 2014 19:21:16 +0000')
```

## set\_headers

```python
message = sendgrid.Mail()
message.set_headers({'X-Sent-Using': 'SendGrid-API', 'X-Transport': 'web'});
```

<a name="set_file_attachments"></a>
# SET FILE ATTACHEMENTS

There are multiple ways to work with attachments:

## add\_attachment

```python
message = sendgrid.Mail()
message.add_attachment('stuff.txt', './stuff.txt')
# or
message.add_attachment('stuff.txt', open('./stuff.txt', 'rb'))
```

## add\_attachment\_stream

```python
message = sendgrid.Mail()
message.add_attachment_stream('filename', 'somerandomcontentyouwant')
# strings, unicode, or BytesIO streams
```

## add\_content\_id

```python
message = sendgrid.Mail()
message.add_attachment('image.png', open('./image.png', 'rb'))
message.add_content_id('image.png', 'ID_IN_HTML')
message.set_html('<html><body>TEXT BEFORE IMAGE<img src="cid:ID_IN_HTML"></img>AFTER IMAGE</body></html>')
```

<a name="smtpapi"></a>
# SendGrid's [X-SMTPAPI](http://sendgrid.com/docs/API_Reference/SMTP_API/)

If you wish to use the X-SMTPAPI on your own app, you can use the
[SMTPAPI Python library](https://github.com/sendgrid/smtpapi-python).

There are implementations for setter methods too.

## Example

```python
sg = sendgrid.SendGridClient('SENDGRID_API_KEY')
message = sendgrid.Mail()
message.add_substitution(':first_name', 'John')
message.smtpapi.add_to('John <example@example.com>')
message.set_subject('Testing from the Python library using the SMTPAPI')
message.set_html('<b>:first_name, this was a successful test of using the SMTPAPI library!</b>')
message.set_text(':name, this was a successful test of using the SMTPAPI library!')
message.set_from('Jane <example@example.com>')
sg.send(message)
```

## Recipients\_

```python
message = sendgrid.Mail()
message.smtpapi.add_to('example@email.com')
```

## [Substitution](http://sendgrid.com/docs/API_Reference/SMTP_API/substitution_tags.html)

```python
message = sendgrid.Mail()
message.smtpapi.add_substitution('key', 'value')
```

### add\_substitution

```python
message = sendgrid.Mail()
message.add_substitution('key', 'value')
```

### set\_substitutions

```python
message = sendgrid.Mail()
message.set_substitutions({'key1': ['value1', 'value2'], 'key2': ['value3', 'value4']})
```

## [Section](http://sendgrid.com/docs/API_Reference/SMTP_API/section_tags.html)

```python
message = sendgrid.Mail()
message.smtpapi.add_section('section', 'value')
```

### add\_section

```python
message = sendgrid.Mail()
message.add_section('section', 'value')
```

### set\_sections

```python
message = sendgrid.Mail()
message.set_sections({'section1': 'value1', 'section2': 'value2'})
```

## [Category](http://sendgrid.com/docs/Delivery_Metrics/categories.html)

```python
message = sendgrid.Mail()
message.smtpapi.add_category('category')
```

### add\_category

```python
message = sendgrid.Mail()
message.add_category('category')
```

### set\_categories

```python
message = sendgrid.Mail()
message.set_categories(['category1', 'category2'])
```

## [Unique Arguments](http://sendgrid.com/docs/API_Reference/SMTP_API/unique_arguments.html)

```python
message = sendgrid.Mail()
message.smtpapi.add_unique_arg('key', 'value')
```

### add\_unique\_arg

```python
message = sendgrid.Mail()
message.add_unique_arg('key', 'value')
```

### set\_unique\_args

```python
message = sendgrid.Mail()
message.set_unique_args({'key1': 'value1', 'key2': 'value2'})
```

## [Filter](http://sendgrid.com/docs/API_Reference/SMTP_API/apps.html)

```python
message = sendgrid.Mail()
message.smtpapi.add_filter('filter', 'setting', 'value')
```

### add\_filter

```python
message = sendgrid.Mail()
message.add_filter('filter', 'setting', 'value')
```

## ASM Group\_

```python
message = sendgrid.Mail()
message.smtpapi.set_asm_group_id(value)
```

### set\_asm\_group\_id

```python
message = sendgrid.Mail()
message.set_asm_group_id(value)
```

<a name="template_engine"></a>
# USING TEMPLATES FROM THE TEMPLATE ENGINE

```python
message.add_filter('templates', 'enable', '1')
message.add_filter('templates', 'template_id', 'TEMPLATE-ALPHA-NUMERIC-ID')
message.add_substitution('key', 'value')
```

<a name="error_handling"></a>
# ERROR HANDLING

By default, `.send` method returns a tuple
`(http_status_code, message)`, however you can pass `raise_errors=True`
to `SendGridClient` constructor, then `.send` method will raise
`SendGridClientError` for 4xx errors, and `SendGridServerError` for 5xx
errors.

```python
from sendgrid import SendGridError, SendGridClientError, SendGridServerError

sg = sendgrid.SendGridClient('YOUR_SENDGRID_API_KEY', None, raise_errors=True)

try:
    sg.send(message)
except SendGridClientError:
    ...
except SendGridServerError:
    ...
```