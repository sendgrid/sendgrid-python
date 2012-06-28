import unittest
import sendgrid


class TestMessage(unittest.TestCase):
    def test_message_construction(self):
        # set string from address
        message = sendgrid.Message("example@example.com", "subject1", "plain_text", "html")
        self.assertEqual(message.from_name, '', "From name is empty")
        self.assertEqual(message.from_address, 'example@example.com', "From address is set")

        # set tuple from address
        message = sendgrid.Message(("example1@example.com", "John, Doe"), "subject1", "plain_text", "html")
        self.assertEqual(message.from_name, 'John, Doe', "From name is set")
        self.assertEqual(message.from_address, 'example1@example.com', "From address is set")

        # omit html and text parameter
        self.assertRaises(ValueError, sendgrid.Message, ("example1@example.com", "John, Doe"), "subject1")

        # pass html only
        sendgrid.Message(("example1@example.com", "John, Doe"), "subject1", html="html")

        # pass text only
        sendgrid.Message(("example1@example.com", "John, Doe"), "subject1", text="text")

        # pass None for html
        sendgrid.Message(("example1@example.com", "John, Doe"), "subject1", text="text", html=None)

        # pass None for text
        sendgrid.Message(("example1@example.com", "John, Doe"), "subject1", html="html", text=None)


    def test_recipients_adding(self):
        message = sendgrid.Message("example@example.com", "subject1", "plain_text", "html")
        message.add_to("example@example.com", "John Doe")
        self.assertEqual(message.to, ["example@example.com"], "Single email address added")
        self.assertEqual(message.to_name, ["John Doe"], "Single email address added")

        message.add_to(["example1@example.com", "example2@example.com"], ("John Doe", "Jane Doe"))
        self.assertEqual(message.to, ["example@example.com","example1@example.com","example2@example.com",],
            "Email list added")
        self.assertEqual(message.to_name, ["John Doe","John Doe","Jane Doe",], "Email list added")

        # following should replace existing to addresses and use x-smtpapi header instead
        message = sendgrid.Message("example@example.com", "subject1", "plain_text", "html")
        #invalid data
        data = {
            'example1@example.com': {'name': 'Name 1', 'code': 'Code 1'},
            'example2@example.com': {'name': 'Name 2'},
            }
        self.assertRaises(ValueError, message.add_to, data)

        #valid data
        data = {
            'example1@example.com': {'name': 'Name 1', 'code': 'Code 1'},
            'example2@example.com': {'name': 'Name 2', 'code': 'Code 2'},
            }
        message.add_to(data)
        self.assertEqual(message.header.as_json(),
            '{"to": ["example1@example.com", "example2@example.com"], "sub": {"code": ["Code 1", "Code 2"], "name": ["Name 1", "Name 2"]}}')
        self.assertEqual(message.to, ["example1@example.com"])
        self.assertEqual(len(message.to), 1)


    def test_cc_bcc__attachment_adding(self):
        message = sendgrid.Message("example@example.com", "subject1", "plain_text", "html")
        message.add_cc("example@example.com")
        self.assertEqual(message.cc, ["example@example.com"], "CC address added")

        message.add_cc(["example1@example.com", "example2@example.com"])
        self.assertEqual(message.cc, ["example@example.com", "example1@example.com", "example2@example.com"],
            "CC address added")

        message.add_bcc("example@example.com")
        self.assertEqual(message.bcc, ["example@example.com"], "BCC address added")

        message.add_bcc(["example1@example.com", "example2@example.com"])
        self.assertEqual(message.bcc, ["example@example.com", "example1@example.com", "example2@example.com"],
            "BCC address added")

        message.add_attachment("file1.txt", "File data")
        self.assertEqual(message.attachments, [{'name': 'file1.txt', 'file': 'File data', 'cid': None}],
            "File attachment added")


    def test_header_functions(self):
        # add categories
        message = sendgrid.Message("example@example.com", "subject1", "plain_text", "html")
        message.add_category("category 1")
        self.assertEqual(message.header.as_json(), '{"category": ["category 1"]}', "Category added")

        message.add_category(["category 2", "category 3"])
        self.assertEqual(message.header.as_json(), '{"category": ["category 1", "category 2", "category 3"]}',
            "Category list added")

        # add unique arguments
        message = sendgrid.Message("example@example.com", "subject1", "plain_text", "html")
        message.set_unique_arguments({"customerAccountNumber": "55555", "activationAttempt": "1"})
        self.assertEqual(message.header.as_json(), '{"unique_args": {"activationAttempt": "1", "customerAccountNumber": "55555"}}',
            "Unique arguments added")

        message.add_unique_argument("test", "some_value")
        self.assertEqual(message.header.as_json(), '{"unique_args": {"test": "some_value", "activationAttempt": "1", "customerAccountNumber": "55555"}}',
            "Unique argument added")

        # add header
        message = sendgrid.Message("example@example.com", "subject1", "plain_text", "html")
        message.add_header("x-test", "header1")
        self.assertEqual(message.headers, {"x-test": "header1"}, "Header added")

        # add filter settings
        message = sendgrid.Message("example@example.com", "subject1", "plain_text", "html")
        message.add_filter_setting("gravatar", "enable", 1)
        self.assertEqual(message.header.as_json(), '{"filters": {"gravatar": {"settings": {"enable": 1}}}}',
            "Filter setting added")

        # add sections
        message = sendgrid.Message("example@example.com", "subject1", "plain_text", "html")
        message.set_sections({"section1": "Section1", "section2": "Section2"})
        self.assertEqual(message.header.as_json(), '{"section": {"section2": "Section2", "section1": "Section1"}}',
            "Sections added")

if __name__ == '__main__':
    unittest.main()
