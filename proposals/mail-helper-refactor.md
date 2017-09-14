# Send a Single Email to a Single Recipient

The following code assumes you are storing the API key in an [environment variable (recommended)](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment). If you don't have your key stored in an environment variable, you can assign it directly to `apikey` for testing purposes.

This is the minimum code needed to send an email.

```python
import os
import sendgrid
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent

msg = Mail(from_email=From('from@example.com', 'From Name'),
           to_email=To('to@example.com', 'To Name'),
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
           to_emails=tos,
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
from time import gmtime, strftime
global_substitutions = {
    '-time-': strftime("%Y-%m-%d %H:%M:%S", gmtime())
}
msg = Mail(from_email=From('from@example.com', 'From Name'),
           to_emails=tos,
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

msg.add_to(To('test1@example.com', 'Example User1'))
to_emails = [ 
    To('test2@example.com', 'Example User2'),
    To('test3@example.com', 'Example User3')
]
msg.add_tos(to_emails)

msg.add_cc(Cc('test4@example.com', 'Example User4'))
cc_emails = [ 
    Cc('test5@example.com', 'Example User5'),
    Cc('test6@example.com', 'Example User6')
]
msg.add_ccs(cc_emails)

msg.add_bcc(Bcc('test7@example.com', 'Example User7'))
bcc_emails = [ 
    Bcc('test8@example.com', 'Example User8'),
    Bcc('test9@example.com', 'Example User9')
]
msg.add_bccs(bcc_emails)

msg.add_header(Header('X-Test1', 'Test1'))
msg.add_header(Header('X-Test2', 'Test2'))
headers = [
    Header('X-Test3', 'Test3'),
    Header('X-Test4', 'Test4')
]
msg.add_headers(headers)

msg.add_substitution(Substitution('%name1%', 'Example Name 1'))
msg.add_substitution(Substitution('%city1%', 'Denver'))
substitutions = [
    Substitution('%name2%', 'Example Name 2'),
    Substitution('%city2%', 'Orange')
]
msg.add_substitutions(substitutions)

msg.add_custom_arg(CustomArg('marketing1', 'false'))
msg.add_custom_arg(CustomArg('transactional1', 'true'))
custom_args = [
    CustomArg('marketing2', 'true'),
    CustomArg('transactional2', 'false')
]
msg.add_custom_args(custom_args)

msg.set_send_at(1461775051)

msg.set_subject(Subject('this subject overrides the Global Subject on the default Personalization'))

# If you need to add more [Personalizations](https://sendgrid.com/docs/Classroom/Send/v3_Mail_Send/personalizations.html), here is an example of adding another Personalization by passing in a personalization index.

msg.add_to(To('test10@example.com', 'Example User10'), 1)
to_emails = [ 
    To('test11@example.com', 'Example User11'),
    To('test12@example.com', 'Example User12')
]
msg.add_tos(to_emails, 1)

msg.add_cc(Cc('test13@example.com', 'Example User13'), 1)
cc_emails = [ 
    Cc('test14@example.com', 'Example User14'),
    Cc('test15@example.com', 'Example User15')
]
msg.add_ccs(cc_emails, 1)

msg.add_bcc(Bcc('test16@example.com', 'Example User16'), 1)
bcc_emails = [ 
    Bcc('test17@example.com', 'Example User17'),
    Bcc('test18@example.com', 'Example User18')
]
msg.add_bccs(bcc_emails, 1)

msg.add_header(Header('X-Test5', 'Test5'), 1)
msg.add_header(Header('X-Test6', 'Test6'), 1)
headers = [
    Header('X-Test7', 'Test7'),
    Header('X-Test8', 'Test8')
]
msg.add_headers(headers, 1)

msg.add_substitution(Substitution('%name3%', 'Example Name 3'), 1);
msg.add_substitution(Substitution('%city3%', 'Redwood City'), 1);
substitutions = [
    Substitution('%name4%', 'Example Name 4'),
    Substitution('%city4%', 'London')
]
msg.add_substitutions(substitutions, 1)

msg.add_custom_arg(CustomArg('marketing3', 'true'), 1)
msg.add_custom_arg(CustomArg('transactional3', 'false'), 1)
custom_args = [
    CustomArg('marketing4', 'false'),
    CustomArg('transactional4': 'true')
]
msg.add_custom_args(custom_args, 1)

msg.set_send_at(1461775052, 1)

msg.set_subject(Subject('this subject overrides the Global Subject on the second Personalization'), 1)

# The values below this comment are global to entire message

msg.set_from(From('test0@example.com', 'Example User0'))

msg.set_global_subject(Subject('Sending with SendGrid is Fun'));

msg.add_content(Content(MimeType.Text, 'and easy to do anywhere, even with Python'))
msg.add_content(Content(MimeType.Html, '<strong>and easy to do anywhere, even with Python</strong>'))
contents = [
    Content('text/calendar', 'Party Time!!'),
    Content('text/custom', 'Party Time 2!!')
]
msg.add_contents(contents)

msg.add_attachment(Attachment('balance_001.pdf',
                   'base64 encoded content',
                   'application/pdf',
                   'attachment',
                   'Balance Sheet'))

attachments = [
    Attachment('banner.png',
               'base64 encoded content',
               'image/png',
               'inline',
               'Banner'),
    Attachment('banner2.png',
               'base64 encoded content',
               'image/png',
               'inline',
               'Banner 2'),                             
]
msg.add_attachments(attachments)

msg.set_template_id(TemplateId('13b8f94f-bcae-4ec6-b752-70d6cb59f932'))

msg.add_global_header(Header('X-Day', 'Monday'))
global_headers = [
    Header('X-Month', 'January'),
    Header('X-Year': '2017')
]
msg.set_global_headers(global_headers)

msg.add_section(Section('%section1%', 'Substitution for Section 1 Tag'))
sections = [
    Section('%section2%', 'Substitution for Section 2 Tag'),
    Section('%section3%': 'Substitution for Section 3 Tag')    
]
msg.add_sections(sections)

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
           to_email=To('to@example.com', 'To Name'),
           subject=Subject('Sending with SendGrid is Fun'),
           plain_text_content=PlainTextContent('and easy to do anywhere, even with Python'),
           html_content=HtmlContent('<strong>and easy to do anywhere, even with Python</strong>'))
msg.add_attachment(Attachment('balance_001.pdf',
                   'base64 encoded content',
                   'application/pdf',
                   'attachment',
                   'Balance Sheet'))

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
           to_email=To('to@example.com', 'To Name'),
           subject=Subject('Sending with SendGrid is Fun'),
           plain_text_content=PlainTextContent('and easy to do anywhere, even with Python'),
           html_content=HtmlContent('<strong>and easy to do anywhere, even with Python</strong>'))
substitutions = [
    Substitution('-name-', 'Example User'),
    Substitution('-city-', 'Denver')
]
msg.add_substitutions(substitutions)
msg.set_template_id(TemplateId('13b8f94f-bcae-4ec6-b752-70d6cb59f932'))

try:
    response = sendgrid.send(msg, apikey=os.environ.get('SENDGRID_apikey'))
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.read())
```