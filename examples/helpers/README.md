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
The `Content` class takes mainly two parameters - MIME type and the actual content of the email, it then returns the JSON-ready representation of this Content.

```
 mail = Mail(from_email, subject, to_email, content)
```
After adding the above we create a mail object using `Mail` class, it takes the following parameters - Email address to send from, Subject line of emails, Email address to send to,Content of the message.
for more information on parameters and usage, see [here](https://github.com/sendgrid/sendgrid-python/blob/master/sendgrid/helpers/mail/mail.py)

### Creating Personalizations

To create personalizations, you need a dictionary to store all your email components. see example [here](https://github.com/sendgrid/sendgrid-python/blob/0b683169b08d3a7c204107cd333be33053297e74/examples/helpers/mail_example.py#L47)
After creating a dictionary, you can go ahead and create a `Personalization` object. 
```
 mock_personalization = Personalization()
    for to_addr in personalization['to_list']:
       mock_personalization.add_to(to_addr)
```
