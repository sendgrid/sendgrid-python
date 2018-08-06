# Create a Django app to send email with SendGrid

This tutorial explains how we set up a simple Django app to send an email with the SendGrid Python SDK and how we deploy our app to Heroku.

## Create a Django project

We first create a project folder.

```bash
$ mkdir hello-sendgrid
$ cd hello-sendgrid
```

We assume you have created and activated a [virtual environment](https://virtualenv.pypa.io/) (See [venv](https://docs.python.org/3/tutorial/venv.html) for Python 3+) for isolated Python environments.

Run the command below to install Django, Gunicorn (a Python WSGI HTTP server), and SendGrid Python SDK.

```bash
$ pip install django gunicorn sendgrid
```

It's a good practice for Python dependency management. We'll pin the requirements with a file `requirements.txt`.

```bash
$ pip freeze > requirements.txt
```

Run the command below to initialize a Django project.

```bash
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

**Note:** It would be best to change your to email from `test@example.com` to your own email, so that you can see the email you receive.

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

These paths allow the URL `/sendgrid/` to send the email.

We also assume that you have set up your development environment with your `SENDGRID_API_KEY`. If you have not done it yet, please do so. See the section [Setup Environment Variables](https://github.com/sendgrid/sendgrid-python#setup-environment-variables).

Now we should be able to send an email. Let's run our Django development server to test it.

```
$ cd hello_sengrid
$ python manage.py migrate
$ python manage.py runserver
```

By default, it starts the development server at `http://127.0.0.1:8000/`. To test if we can send email or not, go to `http://127.0.0.1:8000/sendgrid/`. If it works, we should see the page says "Email Sent!".

**Note:** If you use `test@example.com` as your from email, it's likely to go to your spam folder. To have the emails show up in your inbox, try using an email address at the domain you registered your SendGrid account.

## Deploy to Heroku

There are different deployment methods we can choose. In this tutorial, we choose to deploy our app using the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli). Therefore, let's install it before we go further.

Once you have the Heroku CLI installed, run the command below to log in to your Heroku account if you haven't already.

```
$ heroku login
```

Before we start the deployment, let's create a Heroku app by running the command below. This tutorial names the Heroku app `hello-sendgrid`.

```bash
$ heroku create hello-sendgrid
```

**Note:** If you see Heroku reply with "Name is already taken", please add a random string to the end of the name.

We also need to do a couple things:

1. Add `'*'` or your Heroku app domain to `ALLOWED_HOSTS` in the file `settings.py`. It will look like this:
```python
ALLOWED_HOSTS = ['*']
```

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

Go to the root folder then initialize a Git repository.

```
$ git init
$ heroku git:remote -a hello-sendgrid
```

**Note:** Change `hello-sendgrid` to your new Heroku app name you created earlier.

Add your `SENDGRID_API_KEY` as one of the Heroku environment variables.

```
$ heroku config:set SENDGRID_API_KEY=<YOUR_SENDGRID_API_KEY>
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

After that, let's verify if our app is working or not by accessing the root domain of your Heroku app. You should see the page says "Email Sent!" and on the Activity Feed page in the SendGrid dashboard, you should see a new feed with the email you set in the code.