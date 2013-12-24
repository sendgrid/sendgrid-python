import os
from sendgrid import SendGridClient, Mail

sg = SendGridClient(os.getenv('SG_USER'), os.getenv('SG_PWD'))
m = Mail(to=['yamil.asusta@upr.edu'])
m.set_from('yamil@sendgrid.com')
m.set_subject('JAJA')
m.set_text('fail')
m.add_attachment_stream('test.txt', 'Testing them string bro')
print str(sg.send(m))
