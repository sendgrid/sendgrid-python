# Transactional Templates

For this example, we assume you have created a [transactional template](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html). Following is the template content we used for testing.

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

### With dynamic templates

Sendgrid dynamic templates let you leverage power of [handlebars](https://handlebarsjs.com/)
syntax to easily manage complex dynamic content in transactional emails.

To check this example snippet, create
[transactional email template](https://sendgrid.com/dynamic_templates) with code like
```html
<p>Hello, {{name}}! Your current balance is {{balance}}<p>
```

Than send email based on it, providing context for substitutions:
```python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email, Personalization


sg = SendGridAPIClient(apikey='SG.your-api-key')

mail = Mail()
mail.from_email='templates@example.com'
mail.template_id = 'd-your-dynamic-template-uid'
p = Personalization()
p.add_to(Email('user@example.com'))
p.dynamic_template_data = {'name': 'Bob', 'balance': 42}
mail.add_personalization(p)

sg.client.mail.send.post(request_body=mail.get())
```

Read more about dynamic templates in [docs](https://sendgrid.com/docs/User_Guide/Transactional_Templates/how_to_send_an_email_with_transactional_templates.html)

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
