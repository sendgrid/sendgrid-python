import os
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import json
import sys
import collections
try:
    from StringIO import StringIO
except ImportError:  # Python 3
    from io import StringIO

from sendgrid import SendGridClient, Mail
from sendgrid.exceptions import SendGridClientError, SendGridServerError
from sendgrid.sendgrid import HTTPError

SG_USER = os.getenv('SG_USER') or 'SENDGRID_USERNAME'
SG_PWD  = os.getenv('SG_PWD') or 'SENDGRID_PASSWORD'

class TestSendGrid(unittest.TestCase):
    
    def setUp(self):
        self.sg = SendGridClient(SG_USER, SG_PWD)
        self.maxDiff = None

    def test_apikey_init(self):
        sg = SendGridClient(SG_PWD)
        self.assertEqual(sg.password, SG_PWD)
        self.assertIsNone(sg.username)

    @unittest.skipUnless(sys.version_info < (3, 0), 'only for python2')
    def test_unicode_recipients(self):
        recipients = [unicode('test@test.com'), unicode('guy@man.com')]
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
        m.set_asm_group_id(42)
        m.add_cc('cc@email.com')
        m.add_bcc('bcc@email.com')
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
                "from": "doe@email.com",
                "cc[]": ["cc@email.com"],
                "bcc[]": ["bcc@email.com"]
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
                },
                "asm_group_id": 42
            }
            '''))
        
        try:
            self.assertItemsEqual(url, test_url)
        except: # Python 3+
            self.assertCountEqual(url, test_url)
        
    @unittest.skipUnless(sys.version_info < (3, 0), 'only for python2')
    def test__build_body_unicode(self):
        """test _build_body() handles encoded unicode outside ascii range"""
        from_email = '\xd0\x9d\xd0\xb8\xd0\xba\xd0\xb0@email.com'
        from_name = '\xd0\x9a\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xb4\xd0\xb8\xd1\x8f'
        subject = '\xd0\x9d\xd0\xb0\xd0\xb4\xd0\xb5\xd0\xb6\xd0\xb4\xd0\xb0'
        text = '\xd0\x9d\xd0\xb0\xd0\xb4\xd0\xb5\xd0\xb6\xd0\xb4\xd0\xb0'
        html = '\xd0\x9d\xd0\xb0\xd0\xb4\xd0\xb5\xd0\xb6\xd0\xb4\xd0\xb0'
        m = Mail()
        m.add_to('John, Doe <john@email.com>')
        m.set_subject(subject)
        m.set_html(html)
        m.set_text(text)
        m.set_from("%s <%s>" % (from_name, from_email))
        url = self.sg._build_body(m)
        self.assertEqual(from_email, url['from'])
        self.assertEqual(from_name, url['fromname'])
        self.assertEqual(subject, url['subject'])
        self.assertEqual(text, url['text'])
        self.assertEqual(html, url['html'])


    def test_smtpapi_add_to(self):
        '''Test that message.to gets a dummy address for the header to work'''
        m = Mail()
        m.smtpapi.add_to('test@email.com')
        m.set_from('jon@doe.com')
        m.set_subject('test')
        url = self.sg._build_body(m)
        url.pop('api_key', None)
        url.pop('api_user', None)
        url.pop('date', None)
        test_url = json.loads('''
            {
                "to[]": ["jon@doe.com"],
                "subject": "test",
                "from": "jon@doe.com"
            }
            ''')
        test_url['x-smtpapi'] = json.dumps(json.loads('''
            {
                "to": ["test@email.com"]
            }
            '''))
        self.assertEqual(url, test_url)

class SendGridClientUnderTest(SendGridClient):

    def _make_request(self, message):
        raise self.error

class TestSendGridErrorHandling(unittest.TestCase):
    def setUp(self):
        self.sg = SendGridClientUnderTest(SG_USER, SG_PWD, raise_errors=True)

    def test_client_raises_clinet_error_in_case_of_4xx(self):
        self.sg.error = HTTPError('url', 403, 'msg', {}, StringIO('body'))
        with self.assertRaises(SendGridClientError):
            self.sg.send(Mail())

    def test_client_raises_clinet_error_in_case_of_5xx(self):
        self.sg.error = HTTPError('url', 503, 'msg', {}, StringIO('body'))
        with self.assertRaises(SendGridServerError):
            self.sg.send(Mail())