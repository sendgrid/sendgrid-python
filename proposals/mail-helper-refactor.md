# Send a Single Email to a Single Recipient

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

This is the minimum code needed to send an email.

```python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, SendGridException

message = Mail(from_email=From('from@example.com', 'From Name'),
               to_emails=To('to@example.com', 'To Name'),
               subject=Subject('Sending with SendGrid is Fun'),
               plain_text_content=PlainTextContent('and easy to do anywhere, even with Python'),
               html_content=HtmlContent('<strong>and easy to do anywhere, even with Python</strong>'))

try:
    sendgrid_client = SendGridAPIClient(apikey=os.environ.get('SENDGRID_apikey'))
    response = sendgrid_client.send(message=message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except SendGridException as e:
    print(e.read())
```

# Send a Single Email to Multiple Recipients

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

```python
import os
import sendgrid
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent

to_emails = [
    To('to0@example.com', 'To Name 0'),
    To('to1@example.com', 'To Name 1')
]
msg = Mail(from_email=From('from@example.com', 'From Name'),
           to_emails=to_emails,
           subject=Subject('Sending with SendGrid is Fun'),
           plain_text_content=PlainTextContent('and easy to do anywhere, even with Python'),
           html_content=HtmlContent('<strong>and easy to do anywhere, even with Python</strong>'))

try:
    response = sendgrid.send(msg, apikey=os.environ.get('SENDGRID_apikey'))
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.read())
```

# Send Multiple Emails to Multiple Recipients

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

```python
import os
import sendgrid
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent

to_emails = [
    To(email='to0@example.com',
       name='To Name 0',
       substitutions={
           '-name-': 'To Name 0',
           '-github-': 'http://github.com/mbernier',
       },
       subject=Subject('Override Global Subject')),
    To(email='to1@example.com',
       name='To Name 1',
       substitutions={
           '-name-': 'To Name 1',
           '-github-': 'http://github.com/thinkingserious',
       })
]
global_substitutions = {
    '-time-': strftime("%Y-%m-%d %H:%M:%S", gmtime())
}
msg = Mail(from_email=From('from@example.com', 'From Name'),
           to_emails=to_emails,
           subject=Subject('Hi -name-'),
           plain_text_content=PlainTextContent('Hello -name-, your github is -github-, email sent at -time-'),
           html_content=HtmlContent('<strong>Hello -name-, your github is <a href=\"-github-\">here</a></strong> email sent at -time-'),
           global_substitutions=global_substitutions)

try:
    response = sendgrid.send(msg, apikey=os.environ.get('SENDGRID_apikey'))
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.read())
```

# Kitchen Sink - an example with all settings used

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

```python
import os
import sendgrid
from sendgrid.helpers.mail import *

msg = Mail(from_email=From('from@example.com', 'From Name'),
           to_email=To('to@example.com', 'To Name'),
           subject=Subject('Sending with SendGrid is Fun'),
           plain_text_content=PlainTextContent('and easy to do anywhere, even with Python'),
           html_content=HtmlContent('<strong>and easy to do anywhere, even with Python</strong>'))

# For a detailed description of each of these settings, please see the [documentation](https://sendgrid.com/docs/API_Reference/api_v3.html).

msg.to = To('test1@example.com', 'Example User1')
msg.to = [ 
    To('test2@example.com', 'Example User2'),
    To('test3@example.com', 'Example User3')
]

msg.cc = Cc('test4@example.com', 'Example User4')
msg.cc = [ 
    Cc('test5@example.com', 'Example User5'),
    Cc('test6@example.com', 'Example User6')
]

msg.bcc = Bcc('test7@example.com', 'Example User7')
msg.bcc = [ 
    Bcc('test8@example.com', 'Example User8'),
    Bcc('test9@example.com', 'Example User9')
]

msg.header = Header('X-Test1', 'Test1')
msg.header = Header('X-Test2', 'Test2')
msg.header = [
    Header('X-Test3', 'Test3'),
    Header('X-Test4', 'Test4')
]

msg.substitution = Substitution('%name1%', 'Example Name 1')
msg.substitution = Substitution('%city1%', 'Denver')
msg.substitution = [
    Substitution('%name2%', 'Example Name 2'),
    Substitution('%city2%', 'Orange')
]

msg.custom_arg = CustomArg('marketing1', 'false')
msg.custom_arg = CustomArg('transactional1', 'true')
msg.custom_arg = [
    CustomArg('marketing2', 'true'),
    CustomArg('transactional2', 'false')
]

msg.send_at = SendAt(1461775051)

# If you need to add more [Personalizations](https://sendgrid.com/docs/Classroom/Send/v3_Mail_Send/personalizations.html), here is an example of adding another Personalization by passing in a personalization index.

msg.to = To('test10@example.com', 'Example User10', p=1)
msg.to = [ 
    To('test11@example.com', 'Example User11', p=1),
    To('test12@example.com', 'Example User12', p=1)
]

msg.cc = Cc('test13@example.com', 'Example User13', p=1)
msg.cc = [ 
    Cc('test14@example.com', 'Example User14', p=1),
    Cc('test15@example.com', 'Example User15', p=1)
]

msg.bcc = Bcc('test16@example.com', 'Example User16', p=1)
msg.bcc = [ 
    Bcc('test17@example.com', 'Example User17', p=1),
    Bcc('test18@example.com', 'Example User18', p=1)
]

msg.header = Header('X-Test5', 'Test5', p=1)
msg.header = Header('X-Test6', 'Test6', p=1)
msg.headers = [
    Header('X-Test7', 'Test7', p=1),
    Header('X-Test8', 'Test8', p=1)
]

msg.substitution = Substitution('%name3%', 'Example Name 3', p=1)
msg.substitution = Substitution('%city3%', 'Redwood City', p=1)
msg.substitution = [
    Substitution('%name4%', 'Example Name 4', p=1),
    Substitution('%city4%', 'London', p=1)
]

msg.custom_arg = CustomArg('marketing3', 'true', p=1)
msg.custom_arg = CustomArg('transactional3', 'false', p=1)
msg.custom_arg = [
    CustomArg('marketing4', 'false', p=1),
    CustomArg('transactional4': 'true', p=1)
]

msg.send_at = SendAt(1461775052, p=1)

# The values below this comment are global to entire message

msg.global_subject = Subject('Sending with SendGrid is Fun')

msg.content = Content(MimeType.Text, 'and easy to do anywhere, even with Python')
msg.content = Content(MimeType.Html, '<strong>and easy to do anywhere, even with Python</strong>')
msg.content = [
    Content('text/calendar', 'Party Time!!'),
    Content('text/custom', 'Party Time 2!!')
]

msg.attachment = Attachment(FileName('balance_001.pdf'),
                            File('base64 encoded content'),
                            Type('application/pdf'),
                            Disposition('attachment'),
                            Name('Balance Sheet'))
msg.attachment = [
    Attachment(FileName('banner.png'),
               File('base64 encoded content'),
               Type('image/png'),
               Disposition('inline'),
               Name('Banner')),
    Attachment(FileName('banner2.png'),
               File('base64 encoded content'),
               Type('image/png'),
               Disposition('inline'),
               Name('Banner 2'))                             
]

msg.template_id = TemplateId('13b8f94f-bcae-4ec6-b752-70d6cb59f932')

msg.global_header = Header('X-Day', 'Monday')
msg.global_headers = [
    Header('X-Month', 'January'),
    Header('X-Year': '2017')
]

msg.section = Section('%section1%', 'Substitution for Section 1 Tag')
msg.section = [
    Section('%section2%', 'Substitution for Section 2 Tag'),
    Section('%section3%': 'Substitution for Section 3 Tag')    
]

try:
    response = sendgrid.send(msg, apikey=os.environ.get('SENDGRID_apikey'))
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.read())
```

# Attachments

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

```python
import os
import sendgrid
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, Attachment

msg = Mail(from_email=From('from@example.com', 'From Name'),
           to_emails=To('to@example.com', 'To Name'),
           subject=Subject('Sending with SendGrid is Fun'),
           plain_text_content=PlainTextContent('and easy to do anywhere, even with Python'),
           html_content=HtmlContent('<strong>and easy to do anywhere, even with Python</strong>'))
msg.attachment = Attachment(FileName('balance_001.pdf'),
                            File('base64 encoded content'),
                            Type('application/pdf'),
                            Disposition('attachment'),
                            Name('Balance Sheet'))

try:
    response = sendgrid.send(msg, apikey=os.environ.get('SENDGRID_apikey'))
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.read())
```

# Transactional Templates

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

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

```python
import os
import sendgrid
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, Attachment

msg = Mail(from_email=From('from@example.com', 'From Name'),
           to_emails=To('to@example.com', 'To Name'),
           subject=Subject('Sending with SendGrid is Fun'),
           plain_text_content=PlainTextContent('and easy to do anywhere, even with Python'),
           html_content=HtmlContent('<strong>and easy to do anywhere, even with Python</strong>'))
msg.substitution = [
    Substitution('-name-', 'Example User'),
    Substitution('-city-', 'Denver')
]
msg.template_id = TemplateId('13b8f94f-bcae-4ec6-b752-70d6cb59f932')

try:
    response = sendgrid.send(msg, apikey=os.environ.get('SENDGRID_apikey'))
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.read())
```
