# Deploy a simple Hello Email app on AWS

This tutorial explains how to set up a simple "Hello Email" app on AWS, using the AWS CodeStar service.

We'll be creating a basic web service to send email via SendGrid. The application will run on AWS Lambda, and the "endpoint" will be via AWS API Gateway.

The neat thing is that CodeStar provides all of this in a pre-configured package. We just have to make some config changes, and push our code.

Once this tutorial is complete, you'll have a basic web service for sending email that can be invoked via a link to your newly created API endpoint.

### Prerequisites
Python 2.7 and 3.4 or 3.5 are supported by the sendgrid Python library, however I was able to utilize 3.6 with no issue.

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
Log in to your SendGrid account. Click on your user name on the left hand side of the UI and choose "Setup Guide" from the drop-down menu. On the "Welcome" menu, choose "Send Your First Email", and then "Integrate using our Web API or SMTP relay." Choose "Web API" as the recommended option on the next screen, as we'll be using that for this tutorial.  For more information about creating API keys, see https://sendgrid.com/docs/Classroom/Send/How_Emails_Are_Sent/api_keys.html

On the next menu, you have the option to choose what programming language you'll be using. The obvious choice for this tutorial will be Python.

Follow the steps on the next screen. Choose a name for your API key, such as "hello-email". Follow the remaining steps to create an environment variable, install the sendgrid module, and copy the test code. Once that is complete, check the "I've integrated the code above" box, and click the "Next: Verify Integration" button.

Assuming all the steps were completed correctly, you should be greeted with a success message. If not, go back and verify that everything is correct, including your API key environment varible, and Python code.

## Deploy hello-world app using CodeStar

For the rest of the tutorial, we'll be working out of the git repository we cloned from AWS earlier:
```
$ cd hello-email
```
note: this assumes you cloned the Git repo inside your current directory. My directory is:

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

Scroll down to the "Environment Variables" section. Here we need to populate our SendGrid API key. Copy the value from the `.env` file you created earlier, ensuring to capture the entire value. Make sure the key is titled:

```
SENDGRID_API_KEY
```

Now, go back to your project dashboard in CodeStar. Click on the link under "Application endpoints". After a moment, you should be greeted with JSON output indicating an email was successfully sent.

Congratulations, you've just used serverless technology to create an email sending app in AWS!
