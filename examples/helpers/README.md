## Using helper class to send emails
You can use helper classes to customize the process of sending emails using SendGrid. Each process (such as sending a mock email,
building attachments, configuring settings, building personalizations, etc.) are made easy using helpers. All you need is a file with 
all the classes imported and you can start sending emails!

> Note: You will need move this file to the root directory of this project to execute properly.

### Creating a simple email object and sending it
The example [here](https://github.com/sendgrid/sendgrid-python/blob/0b683169b08d3a7c204107cd333be33053297e74/examples/helpers/mail_example.py#L9)
defines minimum requirement to send an email.
```
 from_email = Email("test@example.com")
 subject = "Hello World from the SendGrid Python Library"
 to_email = Email("test@example.com")
```
You can use `Email` class to define a mail id.

```
content = Content("text/plain", "some text here")
```
The `Content` class takes mainly two parameters: MIME type and the actual content of the email, it then returns the JSON-ready representation of this content.

```
 mail = Mail(from_email, subject, to_email, content)
```
After adding the above we create a mail object using `Mail` class, it takes the following parameters: email address to send from, subject line of emails, email address to send to, content of the message.
For more information on parameters and usage, see [here](https://github.com/sendgrid/sendgrid-python/blob/master/sendgrid/helpers/mail/mail.py)

### Creating Personalizations

To create personalizations, you need a dictionary to store all your email components. See example [here](https://github.com/sendgrid/sendgrid-python/blob/0b683169b08d3a7c204107cd333be33053297e74/examples/helpers/mail_example.py#L47)
After creating a dictionary, you can go ahead and create a `Personalization` object. 
```
 mock_personalization = Personalization()
    for to_addr in personalization['to_list']:
       mock_personalization.add_to(to_addr)
```

### Creating Attachments

To create attachments, we use the `Attachment` class and make sure the content is base64 encoded before passing it into attachment.content.
```
    attachment = Attachment()
    attachment.content = ("TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNl"
                          "Y3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gQ3JhcyBwdW12")
```
Another example: [Link](https://github.com/sendgrid/sendgrid-python/blob/master/use_cases/attachment.md)

### Managing Settings

To configure settings in mail, you can use the `MailSettings` class. The class takes some [parameters](https://github.com/sendgrid/sendgrid-python/blob/master/sendgrid/helpers/mail/mail_settings.py#L1)(such as bcc_settings, bypass_list_management, footer_settings, sandbox_mode)

To add tracking settings, you can add `TrackingSettings` class. See example [here](https://github.com/sendgrid/sendgrid-python/blob/master/examples/helpers/mail_example.py#L118) and parameters and usage [here](https://github.com/sendgrid/sendgrid-python/blob/master/sendgrid/helpers/mail/tracking_settings.py).

### Sending email

After you have configured every component and added your own functions, you can send emails.
```
    sg = SendGridAPIClient()
    data = build_kitchen_sink()
    response = sg.client.mail.send.post(request_body=data)
```
Make sure you have [environment variable](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment-variables-and-your-sendgrid-api-key) set up!
Full example [here](https://github.com/sendgrid/sendgrid-python/blob/0b683169b08d3a7c204107cd333be33053297e74/examples/helpers/mail_example.py#L203).

### Using Dynamic Templates
You can use dynamic (handlebars) transactional templates to make things easy and less time taking. To make this work, you should have dynamic template created within your SendGrid account.

See Full example [here](https://github.com/sendgrid/sendgrid-python/blob/0b683169b08d3a7c204107cd333be33053297e74/examples/helpers/mail_example.py#L221).
