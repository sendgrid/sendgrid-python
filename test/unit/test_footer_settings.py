import unittest

from sendgrid.helpers.mail import FooterHtml, FooterSettings, FooterText


class FooterSettingsTests(unittest.TestCase):
    def test_string_constructor_arguments(self):
        footer = FooterSettings(True, 'footer', '<p>footer</p>')
        self.assertEqual(footer.get(), {
            'enable': True, 'text': 'footer', 'html': '<p>footer</p>'})

    def test_string_property_assignment(self):
        footer = FooterSettings()
        footer.text = 'footer'
        footer.html = '<p>footer</p>'
        self.assertEqual(footer.get(), {
            'text': 'footer', 'html': '<p>footer</p>'})

    def test_empty_strings_are_preserved(self):
        footer = FooterSettings(False, '', '')
        self.assertEqual(footer.get(), {
            'enable': False, 'text': '', 'html': ''})

    def test_wrapped_values_are_preserved(self):
        text = FooterText('footer')
        html = FooterHtml('<p>footer</p>')
        footer = FooterSettings(text=text, html=html)
        self.assertIs(footer.text, text)
        self.assertIs(footer.html, html)
        self.assertEqual(footer.get(), {
            'text': 'footer', 'html': '<p>footer</p>'})

    def test_none_clears_properties(self):
        footer = FooterSettings(text=FooterText('footer'),
                                html=FooterHtml('<p>footer</p>'))
        footer.text = None
        footer.html = None
        self.assertEqual(footer.get(), {})
