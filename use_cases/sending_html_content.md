# Sending HTML-only Content


Currently, we require both HTML and Plain Text content for improved deliverability. In some cases, only HTML may be available. The below example shows how to obtain the Plain Text equivalent of the HTML content.

## Using `beautifulsoup4`

```python
import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, Mail
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

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("test@exmaple.com")
subject = "subject"
to_emila = Email("to_email@example.com")
html_content = Content("text/html", html_text)

mail = Mail(from_email, subject, to_email, html_content)

soup = BeautifulSoup(html_text)
plain_text = soup.get_text()
plain_content = Content("text/plain", plain_text)
mail.add_content(plain_content)

try:
    response = sg.client.mail.send.post(request_body=mail.get())
except urllib.HTTPError as e:
    print(e.read())
    exit()

print(response.status_code)
print(response.body)
print(response.headers)
```