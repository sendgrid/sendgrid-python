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

# # Send Multiple Emails to Multiple Recipients

# import os
# import json
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, SendGridException, Substitution
# import time
# import datetime

# to_emails = [
#     To(email='elmer.thomas@sendgrid.com',
#        name='Elmer SendGrid',
#        substitutions={
#            Substitution('-name-', 'Elmer SendGrid'),
#            Substitution('-github-', 'http://github.com/ethomas'),
#        },
#        subject=Subject('Override Global Subject')),
#     To(email='elmer.thomas@gmail.com',
#        name='Elmer Thomas',
#        substitutions={
#            Substitution('-name-', 'Elmer Thomas'),
#            Substitution('-github-', 'http://github.com/thinkingserious'),
#        })
# ]
# ts = time.time()
# global_substitutions = Substitution('-time-', datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
# message = Mail(from_email=From('dx@sendgrid.com', 'DX'),
#                to_emails=to_emails,
#                subject=Subject('Hi -name-'),
#                plain_text_content=PlainTextContent('Hello -name-, your github is -github-, email sent at -time-'),
#                html_content=HtmlContent('<strong>Hello -name-, your github is <a href=\"-github-\">here</a></strong> email sent at -time-'),
#                global_substitutions=global_substitutions,
#                is_multiple=True)

# try:
#     sendgrid_client = SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
#     print(json.dumps(message.get(), sort_keys=True, indent=4))
#     response = sendgrid_client.send(message=message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except SendGridException as e:
#     print(e.message)

# Kitchen Sink - an example with all settings used

import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From, To, Cc, Bcc, Subject, PlainTextContent, HtmlContent, SendGridException, Substitution, Header
import time
import datetime

message = Mail()

message.to = To('elmer+test1@sendgrid.com', 'Example User1')
message.to = [ 
    To('elmer+test2@sendgrid.com', 'Example User2'),
    To('elmer+test3@sendgrid.com', 'Example User3')
]

message.cc = Cc('test4@example.com', 'Example User4')
message.cc = [ 
    Cc('test5@example.com', 'Example User5'),
    Cc('test6@example.com', 'Example User6')
]

message.bcc = Bcc('test7@example.com', 'Example User7')
message.bcc = [ 
    Bcc('test8@example.com', 'Example User8'),
    Bcc('test9@example.com', 'Example User9')
]

# message.header = Header('X-Test1', 'Test1')
# message.header = Header('X-Test2', 'Test2')
# message.header = [
#     Header('X-Test3', 'Test3'),
#     Header('X-Test4', 'Test4')
# ]

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
