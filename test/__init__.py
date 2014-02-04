import os
import unittest
import json
from sendgrid import SendGridClient, Mail

class TestSendGrid(unittest.TestCase):

  def setUp(self):
    self.sg = SendGridClient(os.getenv('SG_USER'), os.getenv('SG_PWD'))

  def test_send(self):
    m = Mail()
    m.add_to('John, Doe <john@email.com>')
    m.set_subject('test')
    m.set_html('WIN')
    m.set_text('WIN')
    m.set_from('doe@email.com')
    m.add_substitution('subKey', 'subValue')
    m.add_section('testSection', 'sectionValue')
    m.add_category('testCategory')
    m.add_unique_arg('testUnique', 'uniqueValue')
    m.add_filter('testFilter', 'filter', 'filterValue')
    m.add_attachment_stream('testFile', 'fileValue')
    self.sg.send(m)
    url = self.sg._build_body(m)
    url.pop('api_key', None)
    url.pop('api_user', None)
    url.pop('date', None)
    testUrl = json.loads('''{"to[]": ["john@email.com"],
    "toname[]": ["John Doe"],
    "html": "WIN",
    "text": "WIN",
    "subject": "test",
    "files[testFile]": "fileValue",
    "from": "doe@email.com",
    "headers": "",
    "fromname": "",
    "replyto": ""}''')
    testUrl['x-smtpapi'] = json.dumps(json.loads('''{"sub":{"subKey":["subValue"]},
      "section":{"testSection":"sectionValue"},
      "category":["testCategory"],
      "unique_args":{"testUnique":"uniqueValue"},
      "filters":{"testFilter":{"settings":{"filter":"filterValue"}}}}'''))
    self.assertEqual(url, testUrl)

if __name__ == '__main__':
  unittest.main()
