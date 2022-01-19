# Transactional Templates

For this example, we assume you have created a [dynamic transactional template](https://sendgrid.com/docs/ui/sending-email/how-to-send-an-email-with-dynamic-transactional-templates/) in the UI or via the API. Following is the template content we used for testing.

Email Subject:

```text
{{ subject }}
```

Template Body:

```html
<html>
<head>
    <title></title>
</head>
<body>
Hello {{ name }},
<br /><br/>
I'm glad you are trying out the template feature!
<br /><br/>
I hope you are having a great day in {{ city }} :)
<br /><br/>
</body>
</html>
```

```python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='from_email@example.com',
    to_emails='to@example.com',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
message.dynamic_template_data = {
    'subject': 'Testing Templates',
    'name': 'Some One',
    'city': 'Denver'
}
message.template_id = 'd-f43daeeaef504760851f727007e0b5d0'
try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
```

## Prevent Escaping Characters

Per Handlebars' documentation: If you don't want Handlebars to escape a value, use the "triple-stash", {{{

> If you include the characters ', " or & in a subject line replacement be sure to use three brackets.

Email Subject:

```text
{{{ subject }}}
```

Template Body:

```html
<html>
<head>
    <title></title>
</head>
<body>
Hello {{{ name }}},
<br /><br/>
I'm glad you are trying out the template feature!
<br /><br/>
<%body%>
<br /><br/>
I hope you are having a great day in {{{ city }}} :)
<br /><br/>
</body>
</html>
```

```python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='from_email@example.com',
    to_emails='to@example.com',
    subject='Sending with SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
message.dynamic_template_data = {
    'subject': 'Testing Templates & Stuff',
    'name': 'Some "Testing" One',
    'city': '<b>Denver<b>',
}
message.template_id = 'd-f43daeeaef504760851f727007e0b5d0'
try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
```
