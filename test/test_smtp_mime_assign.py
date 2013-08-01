from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import unittest
import sendgrid
from sendgrid.transport import smtp

class TestSmtpMIMEAssignment(unittest.TestCase):
    def setUp(self):
        self.smtp_obj = smtp.Smtp('username', 'password')

    """
    message generators that should yield a message with an expected MIME type
    """
    def _genPlainTextMessage(self):
        return sendgrid.Message('example@example.com', 'subjct', 'text', '')

    def _genHTMLTextMessage(self):
        return sendgrid.Message('example@example.com',
                                    'subjct',
                                    '',
                                    '<html></html>')

    def _genSimpleAlternativeMessage(self):
        return sendgrid.Message('example@example.com',
                                'subject',
                                'text',
                                'html')

    def _genSimpleRelatedMessage(self):
        message = sendgrid.Message('example@example.com',
                                    'subject',
                                    'text',
                                    '<img src=\"cid:picture1\">')
        message.add_attachment("my_picture.png",
                                "/path/to/my_picture.png",
                                "picture1")
        return message

    def _genSimpleMixedTextMessage(self):
        message = sendgrid.Message('example@example.com',
                                        'subject',
                                        'text',
                                        '')
        message.add_attachment("output_filename.doc",
                                    "/path/to/input_filename.doc")
        return message

    def _genSimpleMixedHTMLMessage(self):
        message = sendgrid.Message('example@example.com',
                                        'subject',
                                        '',
                                        '<html></html>')
        message.add_attachment("output_filename.doc",
                                    "/path/to/input_filename.doc")
        return message

    """
    test functions with no message embedding
    """
    def test_plain_text(self):
        message = self._genPlainTextMessage()
        message_mime = self.smtp_obj._assignMIME(message)

        self.assertTrue(isinstance(message_mime, MIMEText))
        self.assertEqual(message_mime.get_content_subtype(), 'plain')

    def test_html_text(self):
        message = self._genHTMLTextMessage()
        message_mime = self.smtp_obj._assignMIME(message)

        self.assertTrue(isinstance(message_mime, MIMEText))
        self.assertEqual(message_mime.get_content_subtype(), 'html')

    def test_simple_alternative(self):
        message = self._genSimpleAlternativeMessage()
        message_mime = self.smtp_obj._assignMIME(message)

        self.assertTrue(isinstance(message_mime, MIMEMultipart))
        self.assertEqual(message_mime.get_content_subtype(), 'alternative')

    def test_simple_related(self):
        message = self._genSimpleRelatedMessage()
        message_mime = self.smtp_obj._assignMIME(message)

        self.assertTrue(isinstance(message_mime, MIMEMultipart))
        self.assertEqual(message_mime.get_content_subtype(), 'related')

    def test_simple_mixed(self):
        message_text = self._genSimpleMixedTextMessage()
        message_html = self._genSimpleMixedHTMLMessage()
        message_text_mime = self.smtp_obj._assignMIME(message_text)
        message_html_mime = self.smtp_obj._assignMIME(message_html)

        self.assertTrue(isinstance(message_text_mime, MIMEMultipart))
        self.assertTrue(isinstance(message_html_mime, MIMEMultipart))
        self.assertEqual(message_text_mime.get_content_subtype(), 'mixed')
        self.assertEqual(message_html_mime.get_content_subtype(), 'mixed')

    """
    test functions with message embedding
    """
    def test_simple_embedded_mixed(self):
        embedded_message = self._genSimpleAlternativeMessage()
        message = sendgrid.Message('example@example.com',
                                    'subject',
                                    'some text',
                                    embedded_message)
        message_mime = self.smtp_obj._assignMIME(message)
        payload = message_mime.get_payload()

        self.assertTrue(isinstance(message_mime, MIMEMultipart))
        self.assertEqual(message_mime.get_content_subtype(), 'mixed')
        self.assertEqual(len(payload), 2)
        self.assertTrue(isinstance(payload[0], MIMEText))
        self.assertEqual(payload[1].get_content_subtype(), 'alternative')

    def test_multi_embed(self):
        """
        the embed portfolio will be as follows:

            multipart/mixed:
                text
                multipart/mixed:
                    no text
                    multipart/related
        """
        embedded_deep_message = self._genSimpleRelatedMessage()
        embedded_message = sendgrid.Message('example@example.com',
                                            'subject',
                                            '',
                                            embedded_deep_message)
        message = sendgrid.Message('example@example.com',
                                    'subject',
                                    'text',
                                    embedded_message)
        message_mime = self.smtp_obj._assignMIME(message)
        payload = message_mime.get_payload()

        # top level
        self.assertTrue(isinstance(message_mime, MIMEMultipart))
        self.assertEqual(message_mime.get_content_subtype(), 'mixed')
        self.assertEqual(len(payload), 2)
        self.assertTrue(isinstance(payload[0], MIMEText))
        self.assertEqual(payload[1].get_content_subtype(), 'mixed')

        #second level
        message_mime = payload[1]
        payload = message_mime.get_payload()
        self.assertTrue(isinstance(message_mime, MIMEMultipart))
        self.assertEqual(message_mime.get_content_subtype(), 'mixed')
        self.assertEqual(len(payload), 1)
        self.assertTrue(isinstance(payload[0], MIMEMultipart))
        self.assertEqual(payload[0].get_content_subtype(), 'related')


if __name__ == '__main__':
    unittest.main()
