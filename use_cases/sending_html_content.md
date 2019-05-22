# Sending HTML-only Content


Currently, we require both HTML and Plain Text content for improved deliverability. In some cases, only HTML may be available. The below example shows how to obtain the Plain Text equivalent of the HTML content.

## Using `beautifulsoup4`

```python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import From, To, Subject, PlainTextContent, HtmlContent, Mail
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib
from bs4 import BeautifulSoup

html_text = """
<html>
    <body>
        <p>
            Some
            <b>
                bad
                <i>
                    HTML
                </i>
            </b>
        </p>
    </body>
</html>
"""

sendgrid_client = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = From("from_email@exmaple.com")
to_email = Email("to_email@example.com")
subject = Subject("Test Subject")
html_content = HtmlContent(html_text)

soup = BeautifulSoup(html_text)
plain_text = soup.get_text()
plain_text_content = Content("text/plain", plain_text)
mail.add_content(plain_content)

message = Mail(from_email, to_email, subject, plain_text_content, html_content)

try:
    response = sendgrid_client.send(message=message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except urllib.HTTPError as e:
    print(e.read())
    exit()
```