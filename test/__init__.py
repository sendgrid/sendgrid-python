import os
import unittest2 as unittest
import json
import sys
from sendgrid import SendGridClient, Mail

class TestSendGrid(unittest.TestCase):
    def setUp(self):
        self.sg = SendGridClient(os.getenv('SG_USER'), os.getenv('SG_PWD'))

    @unittest.skipUnless(sys.version_info < (3,0), 'only for python2')
    def test_unicode_recipients(self):
        # Even though the test is skipped, its interpreted, therefore,
        # the test will fail. Adding a workaround.

        if sys.hexversion < 0x03000000:
            recipients = [unicode('test@test.com'), unicode('guy@man.com')]
        else:
            recipients = []

        m = Mail(to=recipients,
                 subject='testing',
                 html='awesome',
                 from_email='from@test.com')

        mock = {'to[]': ['test@test.com', 'guy@man.com']}
        result = self.sg._build_body(m)

        self.assertEqual(result['to[]'], mock['to[]'])

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
        url = self.sg._build_body(m)
        url.pop('api_key', None)
        url.pop('api_user', None)
        url.pop('date', None)
        test_url = json.loads('''
            {
                "to[]": ["john@email.com"],
                "toname[]": ["John Doe"],
                "html": "WIN",
                "text": "WIN",
                "subject": "test",
                "files[testFile]": "fileValue",
                "from": "doe@email.com"
            }
            ''')
        test_url['x-smtpapi'] = json.dumps(json.loads('''
            {
                "sub": {
                    "subKey": ["subValue"]
                },
                "section": {
                    "testSection":"sectionValue"
                },
                "category": ["testCategory"],
                "unique_args": {
                    "testUnique":"uniqueValue"
                },
                "filters": {
                    "testFilter": {
                        "settings": {
                            "filter": "filterValue"
                        }
                    }
                }
            }
            '''))
        self.assertEqual(url, test_url)

if __name__ == '__main__':
    unittest.main()
