This documentation provides examples for specific use cases. Please [open an issue](https://github.com/sendgrid/sendgrid-python/issues) or make a pull request for any use cases you would like us to document here. Thank you!

# Table of Contents

* [Transactional Templates](#transactional-templates)
* [Attachment](#attachment)
* [Create a Django app to send email with SendGrid](#create-a-django-app-to-send-email-with-sendgrid)
  * [Deploy to Heroku](#deploy-to-heroku)
* [How to Setup a Domain Whitelabel](#domain_whitelabel)
* [How to View Email Statistics](#email_stats)
* [Asynchronous Mail Send](#asynchronous-mail-send)
* [Error Handling](#error-handling)
* [Deploy A Simple Hello Email App on AWS](#hello_email_on_aws)

<a name="transactional-templates"></a>
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

<a name="create-a-django-app-to-send-email-with-sendgrid"></a>
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

<a href="#deploy-to-heroku"></a>
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

<a name="domain_whitelabel"></a>
# How to Setup a Domain Whitelabel

You can find documentation for how to setup a domain whitelabel via the UI [here](https://sendgrid.com/docs/Classroom/Basics/Whitelabel/setup_domain_whitelabel.html) and via API [here](https://github.com/sendgrid/sendgrid-python/blob/master/USAGE.md#whitelabel).

Find more information about all of SendGrid's whitelabeling related documentation [here](https://sendgrid.com/docs/Classroom/Basics/Whitelabel/index.html).

<a name="email_stats"></a>
# How to View Email Statistics

You can find documentation for how to view your email statistics via the UI [here](https://app.sendgrid.com/statistics) and via API [here](https://github.com/sendgrid/sendgrid-python/blob/master/USAGE.md#stats).

Alternatively, we can post events to a URL of your choice via our [Event Webhook](https://sendgrid.com/docs/API_Reference/Webhooks/event.html) about events that occur as SendGrid processes your email.

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

<a name="error-handling"></a>
# Error Handling
[Custom exceptions](https://github.com/sendgrid/python-http-client/blob/master/python_http_client/exceptions.py) for `python_http_client` are now supported, which can be imported by consuming libraries.

Please see [here](https://github.com/sendgrid/python-http-client/blob/master/python_http_client/exceptions.py) for a list of supported exceptions.

```python
  import sendgrid
  import os
  from sendgrid.helpers.mail import *
  from python_http_client import exceptions

  sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
  from_email = Email("dx@sendgrid.com")
  to_email = Email("elmer.thomas@sendgrid.com")
  subject = "Sending with SendGrid is Fun"
  content = Content("text/plain", "and easy to do anywhere, even with Python")
  mail = Mail(from_email, subject, to_email, content)
  try:
      response = sg.client.mail.send.post(request_body=mail.get())
  except exceptions.BadRequestsError as e:
      print(e.body)
      exit()
  print(response.status_code)
  print(response.body)
  print(response.headers)
```

<a name="hello_email_on_aws"></a>
# Deploy a simple Hello Email app on AWS

This tutorial explains how to set up a simple "Hello Email" app on AWS, using the AWS CodeStar service.

We'll be creating a basic web service to send email via SendGrid. The application will run on AWS Lambda, and the "endpoint" will be via AWS API Gateway.

The neat thing is that CodeStar provides all of this in a pre-configured package. We just have to make some config changes, and push our code.

Once this tutorial is complete, you'll have a basic web service for sending email that can be invoked via a link to your newly created API endpoint.

### Prerequisites
Python 2.6, 2.7, 3.4, or 3.5 are supported by the sendgrid Python library, however I was able to utilize 3.6 with no issue.

Before starting this tutorial, you will need to have access to an AWS account in which you are allowed to provision resources. This tutorial also assumes you've already created a SendGrid account with free-tier access. Finally, it is highly recommended you utilize [virtualenv](https://virtualenv.pypa.io/en/stable/).

*DISCLAIMER*: Any resources provisioned here may result in charges being incurred to your account. Sendgrid is in no way responsible for any billing charges.


## Getting Started

### Create AWS CodeStar Project
Log in to your AWS account and go to the AWS CodeStar service. Click "Start a project". For this tutorial we're going to choose a Python Web service, utilizing AWS Lambda. You can use the filters on the left hand side of the UI to narrow down the available choices. 

After you've selected the template, you're asked to provide a name for your project. Go ahead and name it "hello-email". Once you've entered a name, click "Create Project" in the lower right hand corner. You can then choose which tools you want to use to interact with the project. For this tutorial, we'll be choosing "Command Line". 

Once that is completed, you'll be given some basic steps to get Git installed and setup, and instructions for connecting to the AWS CodeCommit(git) repository. You can either use HTTPS, or SSH. Instructions for setting up either are provided. 

Go ahead and clone the Git repository link after it is created. You may need to click "Skip" in the lower right hand corner to proceed.

Once that's done, you've successfully created a CodeStar project! You should be at the dashboard, with a view of the wiki, change log, build pipeline, and application endpoint. 

### Create SendGrid API Key
Log in to your SendGrid account. Click on your user name on the left hand side of the UI and choose "Setup Guide" from the drop-down menu. On the "Welcome" menu, choose "Send Your First Email", and then "Integrate using our Web API or SMTP relay." Choose "Web API" as the recommended option on the next screen, as we'll be using that for this tutorial.

On the next menu, you have the option to choose what programming language you'll be using. The obvious choice for this tutorial will be Python.

Follow the steps on the next screen. Choose a name for your API key, such as "hello-email". Follow the remaining steps to create an environment variable, install the sendgrid module, and copy the test code. Once that is complete, check the "I've integrated the code above" box, and click the "Next: Verify Integration" button.

Assuming all the steps were completed correctly, you should be greeted with a success message. If not, go back and verify that everything is correct, including your API key environment varible, and Python code.

## Deploy hello-world app using CodeStar

For the rest of the tutorial, we'll be working out of the git repository we cloned from AWS earlier:
```
$ cd hello-email
```
note: this assumes you cloned the git repo inside your current directory. My directory is: 

```
~/projects/hello-email
```

The directory contents should be as follows:

    ├──buildspec.yml
    ├──index.py
    ├──template.yml
    ├──README.md

The `buildspec.yml` file is a YAML definition for the AWS CodeBuild service, and will not need to be modified for this tutorial. The `index.py` is where the application logic will be placed, and the `template.yml` is a YAML definition file for the AWS Lambda function.

We'll start by modifying the `template.yml` file. Copy and paste from the example below, or edit your existing copy to match:

```yaml
AWSTemplateFormatVersion: 2010-09-09
Transform:
- AWS::Serverless-2016-10-31
- AWS::CodeStar

Parameters:
  ProjectId:
    Type: String
    Description: CodeStar projectId used to associate new resources to team members

Resources:
  HelloEmail:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      Runtime: python3.6
      Role:
        Fn::ImportValue:
          !Join ['-', [!Ref 'ProjectId', !Ref 'AWS::Region', 'LambdaTrustRole']]
      Events:
        GetEvent:
          Type: Api
          Properties:
            Path: /
            Method: get
        PostEvent:
          Type: Api
          Properties:
            Path: /
            Method: post
```

In the root project directory, run the following commands:
```
virtualenv venv
source ./venv/bin/activate
```

Prior to being able to deploy our Python code, we'll need to install the sendgrid Python module *locally*. One of the idiosyncracies of AWS Lambda is that all library and module dependencies that aren't part of the standard library have to be included with the code/build artifact. Virtual environments do not translate to the Lambda runtime environment. 

In the root project directory, run the following command:
```
$ pip install sendgrid -t .
```
This will install the module locally to the project dir, where it can be built into the Lambda deployment.

Now go ahead and modify the `index.py` file to match below:

```python
import json
import datetime
import sendgrid
import os
from sendgrid.helpers.mail import *

def handler(event, context):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("test@example.com")
    to_email = Email("test@example.com")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    status = b"{}".decode('utf-8').format(response.status_code)
    body = b"{}".decode('utf-8').format(response.body)
    headers = b"{}".decode('utf-8').format(response.headers)
    data = {
        'status': status,
        'body': body,
        'headers': headers.splitlines(),
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
```

Note that for the most part, we've simply copied the intial code from the API verification with SendGrid. Some slight modifications were needed to allow it to run as a lambda function, and for the output to be passed cleanly from the API endpoint.

Change the `test@example.com` emails appropriately so that you may receive the test email.

Go ahead and commit/push your code:

```
$ git add .
```

```
$ git commit -m 'hello-email app'
```

```
$ git push
```

Once the code is successfully pushed, head back to the AWS CodeStar dashboard for your project. After your commit successfully registers, an automated build and deployment process should kick off. 

One more step left before our application will work correctly. After your code has bee deployed, head to the AWS Lambda console. Click on your function name, which should start with `awscodestar-hello-email-lambda-`, or similar.

Scroll down to the "Environment Variables" section. Here we need to populate our SendGrid API key. Copy the value from the `sendgrid.env` file you created earlier, ensuring to capture the entire value. Make sure the key is titled:

```
SENDGRID_API_KEY
```

Now, go back to your project dashboard in CodeStar. Click on the link under "Application endpoints". After a moment, you should be greeted with JSON output indicating an email was successfully sent. 

Congratulations, you've just used serverless technology to create an email sending app in AWS!
