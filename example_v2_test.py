import sendgrid
import os
if os.path.exists('.env'):
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_API_KEY'))

"""

# Basic Send Example

message = sendgrid.Mail()
message.add_to('Elmer Thomas <elmer.thomas@sendgrid.com>')
message.set_subject('Testing from the Python library')
message.set_html('<b>This was a successful test!</b>')
message.set_text('This was a successful test!')
message.set_from('Elmer Thomas <dx@sendgrid.com>')
status, msg = sg.send(message)
print status
print msg

# SMTPAPI Basic Send Example

message = sendgrid.Mail()
message.add_substitution(':first_name', 'Elmer')
message.smtpapi.add_to('Elmer Thomas <elmer.thomas@sendgrid.com>')
message.set_subject('Testing from the Python library using the SMTPAPI')
message.set_html('<b>:first_name, this was a successful test of using the SMTPAPI library!</b>')
message.set_text(':name, this was a successful test of using the SMTPAPI library!')
message.set_from('Elmer Thomas <dx@sendgrid.com>')
status, msg = sg.send(message)
print status
print msg

# Template Engine Example
#   In the template editor, the subject is <%subject%> and the body is:
#
#   Hello :name,
#   
#   <%body%>
#
#   With Best Regards,
# 
#   Your Library Tester
# 
#  <%subject%> is replaced with the value in message.set_subject
#  <%body%> is replaced with the value in message.set_html and message.set_text
#  :name is replaced with the value in message.add_substitution

message = sendgrid.Mail()
message.add_filter('templates', 'enable', '1')
message.add_filter('templates', 'template_id', 'TEMPLATE-ALPHA-NUMERIC-ID')
message.add_substitution(':name', 'Elmer')
message.add_to('Elmer Thomas <elmer.thomas@sendgrid.com>')
message.set_subject('Testing from the Python library using the SMTPAPI')
message.set_html('<b>This was a successful test of using the SMTPAPI library!</b>')
message.set_text('This was a successful test of using the SMTPAPI library!')
message.set_from('Elmer Thomas <dx@sendgrid.com>')
status, msg = sg.send(message)
print status
print msg
"""
