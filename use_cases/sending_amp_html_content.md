# Sending AMP-HTML Email

Following is an example on how to send an AMP HTML Email.
Currently, we require AMP HTML and any one of HTML or Plain Text content (preferrably both) for improved deliverability or fallback for AMP HTML Email for supporting older clients and showing alternate content after 30 days.

For more information on AMP emails pls check the [official AMP email page](https://amp.dev/about/email/)

```python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# The below amp html email is taken from [Google AMP Hello World Email](https://amp.dev/documentation/examples/introduction/hello_world_email/)
amp_html_content = '''
<!--
## Introduction

Learn how to create your first AMP email. This sample covers the basic structure of AMP emails.
-->

<!-- -->
<!-- Doctype declaration is required. -->
<!doctype html>
<!-- This tells everyone that this is an AMP email. `<html amp4email>` works too. -->
<html ⚡4email>
<!-- ## Head -->
<!-- -->
<head>
  <!-- The charset definition must be the first child of the `<head>` tag. -->
  <meta charset="utf-8">
  <!-- The AMP runtime.-->
  <script async src="https://cdn.ampproject.org/v0.js"></script>
  <!-- The AMP for Email boilerplate.  -->
  <style amp4email-boilerplate>body{visibility:hidden}</style>
  <!-- Import AMP components in the header, for example the `amp-carousel` component. -->
  <script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>
  <!--
    ### Allowed CSS properties and selectors

    All CSS in any AMP document must be included in a `<style amp-custom>` tag within the header as shown above. Inline style attributes are not allowed in AMP.  CSS allowed within email messages vary depending on the email provider. For reference, the list of CSS properties and values allowed in Gmail can be found at [Gmail Supported CSS Properties & Media Queries](https://developers.google.com/gmail/design/reference/supported_css).
  -->
  <style amp-custom>
    .emailbody {
      padding: 16px;
    }
    .helloworld {
      font-family: Helvetica;
      color: red;
      font-size: 24px;
      padding-bottom: 8px;
    }
    .images {
      max-width: 100%;
    }
  </style>
  <!--
    Note: The entire `<style>` tag cannot exceed 75,000 bytes. The validator will check for this.
  -->
<!-- -->
</head>
<!-- ## Body -->
<!-- -->
<body>
  <div class="emailbody">
    <!--
      Just like in AMP web pages, most HTML tags can be used directly.
    -->
    <h1 class="helloworld">Hello!</h1>
    <!--
      Certain tags, such as the `<img>` tag, are replaced with equivalent or slightly enhanced custom AMP HTML tags (see [HTML Tags in the specification](https://github.com/ampproject/amphtml/blob/master/spec/amp-html-format.md)).
    -->
    <amp-img src="https://amp.dev/static/samples/img/amp.jpg" width="800" height="600" layout="responsive"></amp-img>
    <!--
    Important: URLs most use absolute paths in AMP for Email.

    Since we imported the `amp-carousel` component in the header as example, let's try it here.
    -->
    <amp-carousel width="800" height="600" layout="responsive" type="slides" controls>
      <amp-img src="https://amp.dev/static/samples/img/image1.jpg" width="800" height="600" alt="a sample image"></amp-img>
      <amp-img src="https://amp.dev/static/samples/img/image2.jpg" width="800" height="600" alt="another sample image"></amp-img>
      <amp-img src="https://amp.dev/static/samples/img/image3.jpg" width="800" height="600" alt="and another sample image"></amp-img>
    </amp-carousel>
  </div>
</body>
</html>
'''

message = Mail(
    from_email='example@example.com',
    to_emails='example@example.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>',
    amp_html_content=amp_html_content)
try:
    sg =  SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
```