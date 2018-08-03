# Dynamic Transactional Templates

For this example, we assume you have created a [dynamic transactional template](https://sendgrid.com/docs/User_Guide/Transactional_Templates/Create_and_edit_dynamic_transactional_templates.html). Following is the template content we used for testing.

Template ID (replace with your own):

```text
13b8f94f-bcae-4ec6-b752-70d6cb59f932
```

Email Subject:

```text
{{subject}}
```

Template Body:

```html
<html>
<head>
    <title></title>
</head>
<body>
Hello {{name}},
<br /><br/>
I'm glad you are trying out the dynamic template feature!
<br /><br/>
<p align="center">
  <table border="1" cellspacing="0" cellpadding="10">
    <tr>
      <td colspan="2" align="center" bgcolor="#D3D3D3">
        <strong><pre>Values provided</pre></strong>
      </td>
    </tr>
    {{#each this}}
    <tr>
      <td bgcolor="#F8F8F8"><strong><pre>{{@key}}</pre></strong></td>
      <td bgcolor="#FFFFFF"><pre>{{this}}</pre></td>
    </tr>
    {{/each}}
  </table>
</p>
<br /><br/>
I hope you are having a great day :)
<br /><br/>
</body>
</html>
```

## With Mail Helper Class

```python
import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, DynamicTemplateTag, Mail
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
mail.personalizations[0].add_dynamic_template_data(DynamicTemplateTag("name", "Example User"))
mail.personalizations[0].add_dynamic_template_data(DynamicTemplateTag("foo", "bar"))
mail.personalizations[0].add_dynamic_template_data(DynamicTemplateTag("extra", "SG rocks!"))
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

