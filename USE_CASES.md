This documentation provides examples for specific use cases. Please [open an issue](https://github.com/sendgrid/sendgrid-python/issues) or make a pull request for any use cases you would like us to document here. Thank you!

# Table of Contents

* [Transactional Templates](#transactional_templates)
* [Attachment](#attachment)
* [Deploy a Simple Hello Email Django App on Heroku](#hello_email_django_on_heroku)
* [Asynchronous Mail Send](#asynchronous-mail-send)

<a name="transactional_templates"></a>
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

<a name="attachment"></a>
# Attachment

```python
import base64
import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, Mail, Attachment
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("test@example.com")
subject = "subject"
to_email = Email("to_email@example.com")
content = Content("text/html", "I'm a content example")

file_path = "file_path.pdf"
with open(file_path,'rb') as f:
    data = f.read()
    f.close()
encoded = base64.b64encode(data).decode()

attachment = Attachment()
attachment.content = encoded
attachment.type = "application/pdf"
attachment.filename = "test.pdf"
attachment.disposition = "attachment"
attachment.content_id = "Example Content ID"

mail = Mail(from_email, subject, to_email, content)
mail.add_attachment(attachment)
try:
    response = sg.client.mail.send.post(request_body=mail.get())
except urllib.HTTPError as e:
    print(e.read())
    exit()

print(response.status_code)
print(response.body)
print(response.headers)
```

<a name="hello_email_django_on_heroku"></a>
# Deploy a Simple Hello Email Django App on Heroku

This tutorial explains how we set up a simple Django app to send an email with the SendGrid Python SDK and how we deploy our app to Heroku.

## Create a Django project

We first create a project folder.

```
$ mkdir hello-sendgrid
$ cd hello-sendgrid
```

We assume you have created and activated a [virtual environment](https://virtualenv.pypa.io/) (See [venv](https://docs.python.org/3/tutorial/venv.html) for Python 3+) for isolated Python environments.

Run the command below to install Django, Gunicorn (a Python WSGI HTTP server), and SendGrid Python SDK.

```
$ pip install django gunicorn sendgrid
```

It is a good practice for Python dependency management. We will pin the requirements with a file `requirements.txt`.

```
$ pip freeze > requirements.text
```

Run the command below to initialize a Django project.

```
$ django-admin startproject hello_sendgrid
```

The folder structure should look like this:

```
hello-sendgrid
├── hello_sendgrid
│   ├── hello_sendgrid
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
└── requirements.txt
```

Let's create a page to generate and send an email to a user when you hit the page.

We first create a file `views.py` and put it under the folder `hello_sendgrid/hello_sendgrid`. Add the minimum needed code below.

```python
import os

from django.http import HttpResponse

import sendgrid
from sendgrid.helpers.mail import *


def index(request):
    sg = sendgrid.SendGridAPIClient(
        apikey=os.environ.get('SENDGRID_API_KEY')
    )
    from_email = Email('test@example.com')
    to_email = Email('test@example.com')
    subject = 'Sending with SendGrid is Fun'
    content = Content(
        'text/plain',
        'and easy to do anywhere, even with Python'
    )
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

    return HttpResponse('Email Sent!')
```

Now the folder structure should look like this:

```
hello-sendgrid
├── hello_sendgrid
│   ├── hello_sendgrid
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── wsgi.py
│   └── manage.py
└── requirements.txt
```

Next we open the file `urls.py` in order to add the view we have just created to the Django URL dispatcher.

```python
from django.conf.urls import url
from django.contrib import admin

from .views import index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sendgrid/', index, name='sendgrid'),
]
```

We also assume that you have set up your development environment with your `SENDGRID_API_KEY`. If you have not done it yet, please do so. See the section [Setup Environment Variables](https://github.com/sendgrid/sendgrid-python#setup-environment-variables).

Now we should be able to send an email. Let's run our Django development server to test it. Find the file `manage.py` then run:

```
$ python manage.py runserver
```

By default, it starts the development server at `http://127.0.0.1:8000/`. To test if we can send email or not, go to `http://127.0.0.1:8000/sendgrid/`. If it works, we should see the page says "Email Sent!".

## Deploy to Heroku

Before we start the deployment, let's log in to your Heroku account and create a Heroku app. This tutorial uses `hello-sendgrid`.

We also need to do a couple things:

1. Add `'*'` or your Heroku app domain to `ALLOWED_HOSTS` in the file `settings.py`.
2. Add `Procfile` with the code below to declare what commands are run by your application's dynos on the Heroku platform.

```
web: cd hello_sendgrid && gunicorn hello_sendgrid.wsgi --log-file -
```

The final folder structure looks like this:

```
hello-sendgrid
├── hello_sendgrid
│   ├── hello_sendgrid
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── wsgi.py
│   └── manage.py
├── Procfile
└── requirements.txt
```

There are different deployment methods we can choose. In this tutorial, we choose to deploy our app using the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli). Therefore, let's install it before we go further.

Once you have the Heroku CLI installed, run the command below to log in to your Heroku account if you haven't already.

```
$ heroku login
```

Go to the root folder then initialize a Git repository.

```
$ git init
$ heroku git:remote -a hello-sendgrid
```

Since we do not use any static files, we will disable `collectstatic` for this project.

```
$ heroku config:set DISABLE_COLLECTSTATIC=1
```

Commit the code to the repository and deploy it to Heroku using Git.

```
$ git add .
$ git commit -am "Create simple Hello Email Django app using SendGrid"
$ git push heroku master
```

We have not finished yet. We need to go to the Heroku settings and add your `SENDGRID_API_KEY` as one of the Heroku environment variables in the Config Variables section.

After that, let's verify if our app is working or not by accessing the Heroku app domain and going to `/sendgrid/`. You should see the page says "Email Sent!" and on the Activity Feed page in the SendGrid dashboard, you should see a new feed with the email `test@example.com`.

<a name="asynchronous-mail-send"></a>
# Asynchronous Mail Send

## Using `asyncio` (3.5+)

The built-in `asyncio` library can be used to send email in a non-blocking manner. `asyncio` helps us execute mail sending in a separate context, allowing us to continue execution of business logic without waiting for all our emails to send first.

```python
import sendgrid
from sendgrid.helpers.mail import *
import os
import asyncio


sg = sendgrid.SendGridAPIClient(
    apikey=os.getenv("SENDGRID_API_KEY")
)

from_email = Email("test@example.com")
to_email = Email("test1@example.com")

content = Content("text/plain", "This is asynchronous sending test.")

# instantiate `sendgrid.helpers.mail.Mail` objects
em1 = Mail(from_email, "Message #1", to_email, content)
em2 = Mail(from_email, "Message #2", to_email, content)
em3 = Mail(from_email, "Message #3", to_email, content)
em4 = Mail(from_email, "Message #4", to_email, content)
em5 = Mail(from_email, "Message #5", to_email, content)
em6 = Mail(from_email, "Message #6", to_email, content)
em7 = Mail(from_email, "Message #7", to_email, content)
em8 = Mail(from_email, "Message #8", to_email, content)
em9 = Mail(from_email, "Message #9", to_email, content)
em10 = Mail(from_email, "Message #10", to_email, content)


ems = [em1, em2, em3, em4, em5, em6, em7, em8, em9, em10]


async def send_email(n, email):
    '''
    send_mail wraps SendGrid's API client, and makes a POST request to
    the api/v3/mail/send endpoint with `email`.
    Args:
        email<sendgrid.helpers.mail.Mail>: single mail object.
    '''
    try:
        response = sg.client.mail.send.post(request_body=email.get())
        if response.status_code < 300:
            print("Email #{} processed".format(n), response.body, response.status_code)
    except urllib.error.HTTPError as e:
        e.read()


@asyncio.coroutine
def send_many(emails, cb):
    '''
    send_many creates a number of non-blocking tasks (to send email)
    that will run on the existing event loop. Due to non-blocking nature,
    you can include a callback that will run after all tasks have been queued.

    Args:
        emails<list>: contains any # of `sendgrid.helpers.mail.Mail`.
        cb<function>: a function that will execute immediately.
    '''
    print("START - sending emails ...")
    for n, em in enumerate(emails):
        asyncio.async(send_email(n, em))
    print("END - returning control...")
    cb()


def sample_cb():
    print("Executing callback now...")
    for i in range(0, 100):
        print(i)
    return


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = asyncio.async(send_many(ems, sample_cb))
    loop.run_until_complete(task)
```
