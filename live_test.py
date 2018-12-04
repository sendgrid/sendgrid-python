## Send a Single Email to a Single Recipient
# import os
# import json
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, SendGridException

# message = Mail(from_email=From('dx@sendgrid.com', 'DX'),
#                to_emails=To('elmer.thomas@sendgrid.com', 'Elmer Thomas'),
#                subject=Subject('Sending with SendGrid is Fun'),
#                plain_text_content=PlainTextContent('and easy to do anywhere, even with Python'),
#                html_content=HtmlContent('<strong>and easy to do anywhere, even with Python</strong>'))

# try:
#     sendgrid_client = SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
#     print(json.dumps(message.get(), sort_keys=True, indent=4))
#     response = sendgrid_client.send(message=message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except SendGridException as e:
#     print(e.message)

# # Send a Single Email to Multiple Recipients
# import os
# import json
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, SendGridException

# to_emails = [
#     To('elmer.thomas@sendgrid.com', 'Elmer SendGrid'),
#     To('elmer.thomas@gmail.com', 'Elmer Thomas')
# ]
# message = Mail(from_email=From('dx@sendgrid.com', 'DX'),
#                to_emails=to_emails,
#                subject=Subject('Sending with SendGrid is Fun'),
#                plain_text_content=PlainTextContent('and easy to do anywhere, even with Python'),
#                html_content=HtmlContent('<strong>and easy to do anywhere, even with Python</strong>'))

# try:
#     sendgrid_client = SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
#     print(json.dumps(message.get(), sort_keys=True, indent=4))
#     response = sendgrid_client.send(message=message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except SendGridException as e:
#     print(e.message)

# Send Multiple Emails to Multiple Recipients

import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, SendGridException, Substitution
import time
import datetime

to_emails = [
    To(email='elmer.thomas@sendgrid.com',
       name='Elmer SendGrid',
       substitutions={
           Substitution('-name-', 'Elmer SendGrid'),
           Substitution('-github-', 'http://github.com/ethomas'),
       },
       subject=Subject('Override Global Subject')),
    To(email='elmer.thomas@gmail.com',
       name='Elmer Thomas',
       substitutions={
           Substitution('-name-', 'Elmer Thomas'),
           Substitution('-github-', 'http://github.com/thinkingserious'),
       })
]
ts = time.time()
global_substitutions = Substitution('-time-', datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
message = Mail(from_email=From('dx@sendgrid.com', 'DX'),
               to_emails=to_emails,
               subject=Subject('Hi -name-'),
               plain_text_content=PlainTextContent('Hello -name-, your github is -github-, email sent at -time-'),
               html_content=HtmlContent('<strong>Hello -name-, your github is <a href=\"-github-\">here</a></strong> email sent at -time-'),
               global_substitutions=global_substitutions,
               is_multiple=True)

try:
    sendgrid_client = SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    print(json.dumps(message.get(), sort_keys=True, indent=4))
    # response = sendgrid_client.send(message=message)
    # print(response.status_code)
    # print(response.body)
    # print(response.headers)
except SendGridException as e:
    print(e.message)

# ToDo

## The Mail constructor should also support passing in tuples and strings
