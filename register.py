import pypandoc
from io import open

output = pypandoc.convert('README.md', 'rst')
with open('README.txt', 'w+') as f:
    f.write(output)

readme_rst = open('./README.txt', 'r', encoding='utf-8').read()
replace = '''
            .. figure:: https://uiux.s3.amazonaws.com/2016-logos/email-logo
            %402x.png\n   :alt: SendGrid Logo\n\n   SendGrid Logo\n
          '''
replacement = '''
                |SendGrid Logo|\n\n.. |SendGrid Logo| image::
                https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png
                \n   :target: https://www.sendgrid.com
              '''
final_text = readme_rst.replace(replace, replacement)
with open('./README.txt', 'w', encoding='utf-8') as f:
    f.write(final_text)
