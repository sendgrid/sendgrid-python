import sendgrid
import os
if os.path.exists('.env'):
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_USERNAME'), os.environ.get('SENDGRID_PASSWORD'))

"""
to = 'Jane Doe <example@example.com>'
from = 'John Doe <example@example.com>'
message = sendgrid.Mail()
message.add_to(to)
message.set_subject('Testing from the Python library')
message.set_html('<b>This was a successful test!</b>')
message.set_text('This was a successful test!')
message.set_from(from)
status, msg = sg.send(message)
print status
print msg
"""