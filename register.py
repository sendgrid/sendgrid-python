import pypandoc
import os

output = pypandoc.convert('README.md', 'rst')
f = open('README.txt', 'w+')
f.write(str(output.encode('utf-8')))
f.close()

readme_rst = open('./README.txt').read()
replace = '.. figure:: https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png\n   :alt: SendGrid Logo\n\n   SendGrid Logo\n'
replacement = '|SendGrid Logo|\n\n.. |SendGrid Logo| image:: https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png\n   :target: https://www.sendgrid.com'
final_text = readme_rst.replace(replace, replacement)
with open('./README.txt', 'w') as f:
    f.write(final_text)
