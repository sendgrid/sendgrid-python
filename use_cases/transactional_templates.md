### Transactional Templates

SendGrid transactional templates let you leverage power of [handlebars](https://handlebarsjs.com/)
syntax to easily manage complex dynamic content in transactional emails.

For this example, we assume you have created a [transactional template](https://sendgrid.com/docs/User_Guide/Transactional_Templates/create_and_edit_transactional_templates.html). Following is the template content we used for testing.

This example also assumes you [set your environment variable](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment-variables-and-your-sendgrid-api-key) with your SendGrid API Key.

Template ID (replace with your own):

```text
d-13b8f94fbcae4ec6b75270d6cb59f932
```

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
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, Personalization


sg = SendGridAPIClient()
mail = Mail()
mail.from_email = Email('templates@example.com')
mail.template_id = 'd-your-dynamic-template-uid'
p = Personalization()
p.add_to(Email('user@example.com'))
p.dynamic_template_data = {
  'subject': 'Dynamic Templates in Python',
  'name': 'Example User',
  'city': 'Denver'
}
mail.add_personalization(p)

response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.headers)
print(response.body)
```

Read more about dynamic templates [here](https://sendgrid.com/docs/User_Guide/Transactional_Templates/how_to_send_an_email_with_transactional_templates.html).

# Legacy Templates

For this example, we assume you have created a [Legacy Template](https://sendgrid.com/templates). Following is the template content we used for testing.

Template ID (replace with your own):

```text
13b8f94f-bcae-4ec6-b752-70d6cb59f932
```

Email Subject:

```text
<%subject%>
```

Template Body:

```html
<html>
<head>
    <title></title>
</head>
<body>
Hello -name-,
<br /><br/>
I'm glad you are trying out the template feature!
<br /><br/>
<%body%>
<br /><br/>
I hope you are having a great day in -city- :)
<br /><br/>
</body>
</html>
```

## With Mail Helper Class

```python
import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, Substitution, Mail
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("test@example.com")
subject = "I'm replacing the subject tag"
to_email = Email("test@example.com")
content = Content("text/html", "I'm replacing the <strong>body tag</strong>")
mail = Mail(from_email, subject, to_email, content)
mail.personalizations[0].add_substitution(Substitution("-name-", "Example User"))
mail.personalizations[0].add_substitution(Substitution("-city-", "Denver"))
mail.template_id = "13b8f94f-bcae-4ec6-b752-70d6cb59f932"
try:
    response = sg.client.mail.send.post(request_body=mail.get())
except urllib.HTTPError as e:
    print (e.read())
    exit()
print(response.status_code)
print(response.body)
print(response.headers)
```

## Without Mail Helper Class

```python
import sendgrid
import os
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
data = {
  "personalizations": [
    {
      "to": [
        {
          "email": "test@example.com"
        }
      ],
      "substitutions": {
        "-name-": "Example User",
        "-city-": "Denver"
      },
      "subject": "I'm replacing the subject tag"
    },
  ],
  "from": {
    "email": "test@example.com"
  },
  "content": [
    {
      "type": "text/html",
      "value": "I'm replacing the <strong>body tag</strong>"
    }
  ],
  "template_id": "13b8f94f-bcae-4ec6-b752-70d6cb59f932"
}
try:
    response = sg.client.mail.send.post(request_body=data)
except urllib.HTTPError as e:
    print (e.read())
    exit()
print(response.status_code)
print(response.body)
print(response.headers)
```
