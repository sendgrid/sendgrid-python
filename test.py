# -*- coding: utf-8 -*-
import sendgrid
import sys


sg = sendgrid.SendGridClient('tusharb', 'kenshi123')

print sys.getdefaultencoding()
message = sendgrid.Mail(to=['KYÖSTI@tushar.bymail.in', 'KYSTI@tushar.bymail.in'], subject='Example', html='Body', text='Body', from_email='doe@email.com')
print "to message", message.to[0]
status, msg = sg.send(message)
print status, msg