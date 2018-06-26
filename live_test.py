# Send a Single Email to a Single Recipient
import os
from sendgrid import SendGridAPIClient # import sendgrid
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, SendGridException # from sendgrid.helpers.mail

msg = Mail(from_email=From('dx@sendgrid.com', 'DX'),
           to_emails=To('elmer.thomas@sendgrid.com', 'Elmer Thomas'),
           subject=Subject('Sending with SendGrid is Fun'),
           plain_text_content=PlainTextContent('and easy to do anywhere, even with Python'),
           html_content=HtmlContent('<strong>and easy to do anywhere, even with Python</strong>'))

try:
    sg_client = SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    response = sg_client.send(request_body=msg)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except SendGridException as e:
    print(e.message)