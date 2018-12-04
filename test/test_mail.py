# -*- coding: utf-8 -*-
import json
import unittest

try:
    from email.message import EmailMessage
except ImportError:
    # Python2
    from email import message
    EmailMessage = message.Message

from sendgrid.helpers.mail import (
    ASM,
    APIKeyIncludedException,
    Attachment,
    BCCSettings,
    BypassListManagement,
    Category,
    ClickTracking,
    Content,
    CustomArg,
    Email,
    FooterSettings,
    Ganalytics,
    Header,
    Mail,
    MailSettings,
    OpenTracking,
    Personalization,
    SandBoxMode,
    Section,
    SendGridException,
    SpamCheck,
    SubscriptionTracking,
    Substitution,
    TrackingSettings,
    ValidateAPIKey
)


class UnitTests(unittest.TestCase):

    def test_sendgridAPIKey(self):
        """Tests if including SendGrid API will throw an Exception"""

        # Minimum required to send an email
        self.max_diff = None
        mail = Mail()

        mail.from_email = Email("test@example.com")

        mail.subject = "Hello World from the SendGrid Python Library"

        personalization = Personalization()
        personalization.add_to(Email("test@example.com"))
        mail.add_personalization(personalization)

        # Try to include SendGrid API key
        try:
            mail.add_content(Content("text/plain", "some SG.2123b1B.1212lBaC here"))
            mail.add_content(
                Content(
                    "text/html",
                    "<html><body>some SG.Ba2BlJSDba.232Ln2 here</body></html>"))

            self.assertEqual(
                json.dumps(
                    mail.get(),
                    sort_keys=True),
                '{"content": [{"type": "text/plain", "value": "some text here"}, '
                '{"type": "text/html", '
                '"value": "<html><body>some text here</body></html>"}], '
                '"from": {"email": "test@example.com"}, "personalizations": '
                '[{"to": [{"email": "test@example.com"}]}], '
                '"subject": "Hello World from the SendGrid Python Library"}'
            )

        # Exception should be thrown
        except Exception as e:
            pass

        # Exception not thrown
        else:
            self.fail("Should have failed as SendGrid API key included")

    def test_helloEmail(self):
        self.max_diff = None

        """Minimum required to send an email"""
        mail = Mail()

        mail.from_email = Email("test@example.com")

        mail.subject = "Hello World from the SendGrid Python Library"

        personalization = Personalization()
        personalization.add_to(Email("test@example.com"))
        mail.add_personalization(personalization)

        mail.add_content(Content("text/plain", "some text here"))
        mail.add_content(
            Content(
                "text/html",
                "<html><body>some text here</body></html>"))

        self.assertEqual(
            json.dumps(
                mail.get(),
                sort_keys=True),
            '{"content": [{"type": "text/plain", "value": "some text here"}, '
            '{"type": "text/html", '
            '"value": "<html><body>some text here</body></html>"}], '
            '"from": {"email": "test@example.com"}, "personalizations": '
            '[{"to": [{"email": "test@example.com"}]}], '
            '"subject": "Hello World from the SendGrid Python Library"}'
        )

        self.assertIsInstance(str(mail), str)

    def test_helloEmailAdditionalContent(self):
        """Tests bug found in Issue-451 with Content ordering causing a crash"""

        self.maxDiff = None

        """Minimum required to send an email"""
        mail = Mail()

        mail.from_email = Email("test@example.com")

        mail.subject = "Hello World from the SendGrid Python Library"

        personalization = Personalization()
        personalization.add_to(Email("test@example.com"))
        mail.add_personalization(personalization)

        mail.add_content(Content("text/html", "<html><body>some text here</body></html>"))
        mail.add_content(Content("text/plain", "some text here"))

        self.assertEqual(
            json.dumps(
                mail.get(),
                sort_keys=True),
            '{"content": [{"type": "text/plain", "value": "some text here"}, '
            '{"type": "text/html", '
            '"value": "<html><body>some text here</body></html>"}], '
            '"from": {"email": "test@example.com"}, "personalizations": '
            '[{"to": [{"email": "test@example.com"}]}], '
            '"subject": "Hello World from the SendGrid Python Library"}'
        )

        self.assertIsInstance(str(mail), str)

    def test_kitchenSink(self):
        self.max_diff = None

        """All settings set"""
        mail = Mail()

        mail.from_email = Email("test@example.com", "Example User")

        mail.subject = "Hello World from the SendGrid Python Library"

        personalization = Personalization()
        personalization.add_to(Email("test@example.com", "Example User"))
        personalization.add_to(Email("test@example.com", "Example User"))
        personalization.add_cc(Email("test@example.com", "Example User"))
        personalization.add_cc(Email("test@example.com", "Example User"))
        personalization.add_bcc(Email("test@example.com"))
        personalization.add_bcc(Email("test@example.com"))
        personalization.subject = "Hello World from the Personalized SendGrid Python Library"
        personalization.add_header(Header("X-Test", "test"))
        personalization.add_header(Header("X-Mock", "true"))
        personalization.add_substitution(
            Substitution("%name%", "Example User"))
        personalization.add_substitution(Substitution("%city%", "Denver"))
        personalization.add_custom_arg(CustomArg("user_id", "343"))
        personalization.add_custom_arg(CustomArg("type", "marketing"))
        personalization.send_at = 1443636843
        mail.add_personalization(personalization)

        personalization2 = Personalization()
        personalization2.add_to(Email("test@example.com", "Example User"))
        personalization2.add_to(Email("test@example.com", "Example User"))
        personalization2.add_cc(Email("test@example.com", "Example User"))
        personalization2.add_cc(Email("test@example.com", "Example User"))
        personalization2.add_bcc(Email("test@example.com"))
        personalization2.add_bcc(Email("test@example.com"))
        personalization2.subject = "Hello World from the Personalized SendGrid Python Library"
        personalization2.add_header(Header("X-Test", "test"))
        personalization2.add_header(Header("X-Mock", "true"))
        personalization2.add_substitution(
            Substitution("%name%", "Example User"))
        personalization2.add_substitution(Substitution("%city%", "Denver"))
        personalization2.add_custom_arg(CustomArg("user_id", "343"))
        personalization2.add_custom_arg(CustomArg("type", "marketing"))
        personalization2.send_at = 1443636843
        mail.add_personalization(personalization2)

        mail.add_content(Content("text/plain", "some text here"))
        mail.add_content(
            Content(
                "text/html",
                "<html><body>some text here</body></html>"))

        attachment = Attachment()
        attachment.content = "TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gQ3JhcyBwdW12"
        attachment.type = "application/pdf"
        attachment.filename = "balance_001.pdf"
        attachment.disposition = "attachment"
        attachment.content_id = "Balance Sheet"
        mail.add_attachment(attachment)

        attachment2 = Attachment()
        attachment2.content = "BwdW"
        attachment2.type = "image/png"
        attachment2.filename = "banner.png"
        attachment2.disposition = "inline"
        attachment2.content_id = "Banner"
        mail.add_attachment(attachment2)

        mail.template_id = "13b8f94f-bcae-4ec6-b752-70d6cb59f932"

        mail.add_section(
            Section(
                "%section1%",
                "Substitution Text for Section 1"))
        mail.add_section(
            Section(
                "%section2%",
                "Substitution Text for Section 2"))

        mail.add_header(Header("X-Test1", "test1"))
        mail.add_header(Header("X-Test3", "test2"))

        mail.add_header({"X-Test4": "test4"})

        mail.add_category(Category("May"))
        mail.add_category(Category("2016"))

        mail.add_custom_arg(CustomArg("campaign", "welcome"))
        mail.add_custom_arg(CustomArg("weekday", "morning"))

        mail.send_at = 1443636842

        mail.batch_id = "sendgrid_batch_id"

        mail.asm = ASM(99, [4, 5, 6, 7, 8])

        mail.ip_pool_name = "24"

        mail_settings = MailSettings()
        mail_settings.bcc_settings = BCCSettings(
            True, Email("test@example.com"))
        mail_settings.bypass_list_management = BypassListManagement(True)
        mail_settings.footer_settings = FooterSettings(
            True,
            "Footer Text",
            "<html><body>Footer Text</body></html>")
        mail_settings.sandbox_mode = SandBoxMode(True)
        mail_settings.spam_check = SpamCheck(
            True, 1, "https://spamcatcher.sendgrid.com")
        mail.mail_settings = mail_settings

        tracking_settings = TrackingSettings()
        tracking_settings.click_tracking = ClickTracking(
            True, True)
        tracking_settings.open_tracking = OpenTracking(
            True,
            "Optional tag to replace with the open image in the body of the message")
        tracking_settings.subscription_tracking = SubscriptionTracking(
            True,
            "text to insert into the text/plain portion of the message",
            "<html><body>html to insert into the text/html portion of the message</body></html>",
            "Optional tag to replace with the open image in the body of the message")
        tracking_settings.ganalytics = Ganalytics(
            True,
            "some source",
            "some medium",
            "some term",
            "some content",
            "some campaign")
        mail.tracking_settings = tracking_settings

        mail.reply_to = Email("test@example.com")

        expected_result = {
            "asm": {
                "group_id": 99,
                "groups_to_display": [4, 5, 6, 7, 8]
            },
            "attachments": [
                {
                    "content": "TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3"
                               "RldHVyIGFkaXBpc2NpbmcgZWxpdC4gQ3JhcyBwdW12",
                    "content_id": "Balance Sheet",
                    "disposition": "attachment",
                    "filename": "balance_001.pdf",
                    "type": "application/pdf"
                },
                {
                    "content": "BwdW",
                    "content_id": "Banner",
                    "disposition": "inline",
                    "filename": "banner.png",
                    "type": "image/png"
                }
            ],
            "batch_id": "sendgrid_batch_id",
            "categories": [
                "May",
                "2016"
            ],
            "content": [
                {
                    "type": "text/plain",
                    "value": "some text here"
                },
                {
                    "type": "text/html",
                    "value": "<html><body>some text here</body></html>"
                }
            ],
            "custom_args": {
                "campaign": "welcome",
                "weekday": "morning"
            },
            "from": {
                "email": "test@example.com",
                "name": "Example User"
            },
            "headers": {
                "X-Test1": "test1",
                "X-Test3": "test2",
                "X-Test4": "test4"
            },
            "ip_pool_name": "24",
            "mail_settings": {
                "bcc": {
                    "email": "test@example.com",
                    "enable": True
                },
                "bypass_list_management": {
                    "enable": True
                },
                "footer": {
                    "enable": True,
                    "html": "<html><body>Footer Text</body></html>",
                    "text": "Footer Text"
                },
                "sandbox_mode": {
                    "enable": True
                },
                "spam_check": {
                    "enable": True,
                    "post_to_url": "https://spamcatcher.sendgrid.com",
                    "threshold": 1
                }
            },
            "personalizations": [
                {
                    "bcc": [
                        {
                            "email": "test@example.com"
                        },
                        {
                            "email": "test@example.com"
                        }
                    ],
                    "cc": [
                        {
                            "email": "test@example.com",
                            "name": "Example User"
                        },
                        {
                            "email": "test@example.com",
                            "name": "Example User"
                        }
                    ],
                    "custom_args": {
                        "type": "marketing",
                        "user_id": "343"
                    },
                    "headers": {
                        "X-Mock": "true",
                        "X-Test": "test"
                    },
                    "send_at": 1443636843,
                    "subject": "Hello World from the Personalized SendGrid "
                               "Python Library",
                    "substitutions": {
                        "%city%": "Denver",
                        "%name%": "Example User"
                    },
                    "to": [
                        {
                            "email": "test@example.com",
                            "name": "Example User"
                        },
                        {
                            "email": "test@example.com",
                            "name": "Example User"
                        }
                    ]
                },
                {
                    "bcc": [
                        {
                            "email": "test@example.com"
                        },
                        {
                            "email": "test@example.com"
                        }
                    ],
                    "cc": [
                        {
                            "email": "test@example.com",
                            "name": "Example User"
                        },
                        {
                            "email": "test@example.com",
                            "name": "Example User"
                        }
                    ],
                    "custom_args": {
                        "type": "marketing",
                        "user_id": "343"
                    },
                    "headers": {
                        "X-Mock": "true",
                        "X-Test": "test"
                    },
                    "send_at": 1443636843,
                    "subject": "Hello World from the Personalized SendGrid "
                               "Python Library",
                    "substitutions": {
                        "%city%": "Denver",
                        "%name%": "Example User"
                    },
                    "to": [
                        {
                            "email": "test@example.com",
                            "name": "Example User"
                        },
                        {
                            "email": "test@example.com",
                            "name": "Example User"
                        }
                    ]
                }
            ],
            "reply_to": {
                "email": "test@example.com"
            },
            "sections": {
                "%section1%": "Substitution Text for Section 1",
                "%section2%": "Substitution Text for Section 2"
            },
            "send_at": 1443636842,
            "subject": "Hello World from the SendGrid Python Library",
            "template_id": "13b8f94f-bcae-4ec6-b752-70d6cb59f932",
            "tracking_settings": {
                "click_tracking": {
                    "enable": True,
                    "enable_text": True
                },
                "ganalytics": {
                    "enable": True,
                    "utm_campaign": "some campaign",
                    "utm_content": "some content",
                    "utm_medium": "some medium",
                    "utm_source": "some source",
                    "utm_term": "some term"
                },
                "open_tracking": {
                    "enable": True,
                    "substitution_tag": "Optional tag to replace with the "
                                        "open image in the body of the message"
                },
                "subscription_tracking": {
                    "enable": True,
                    "html": "<html><body>html to insert into the text/html "
                            "portion of the message</body></html>",
                    "substitution_tag": "Optional tag to replace with the open"
                                        " image in the body of the message",
                    "text": "text to insert into the text/plain portion of"
                            " the message"
                }
            }
        }
        self.assertEqual(
            json.dumps(mail.get(), sort_keys=True),
            json.dumps(expected_result, sort_keys=True)
        )

    def test_unicode_values_in_substitutions_helper(self):
        """ Test that the Substitutions helper accepts unicode values """

        self.max_diff = None

        """Minimum required to send an email"""
        mail = Mail()

        mail.from_email = Email("test@example.com")

        mail.subject = "Testing unicode substitutions with the SendGrid Python Library"

        personalization = Personalization()
        personalization.add_to(Email("test@example.com"))
        personalization.add_substitution(Substitution("%city%", u"Αθήνα"))
        mail.add_personalization(personalization)

        mail.add_content(Content("text/plain", "some text here"))
        mail.add_content(
            Content(
                "text/html",
                "<html><body>some text here</body></html>"))

        expected_result = {
            "content": [
                {
                    "type": "text/plain",
                    "value": "some text here"
                },
                {
                    "type": "text/html",
                    "value": "<html><body>some text here</body></html>"
                }
            ],
            "from": {
                "email": "test@example.com"
            },
            "personalizations": [
                {
                    "substitutions": {
                        "%city%": u"Αθήνα"
                    },
                    "to": [
                        {
                            "email": "test@example.com"
                        }
                    ]
                }
            ],
            "subject": "Testing unicode substitutions with the SendGrid Python Library",
        }

        self.assertEqual(
            json.dumps(mail.get(), sort_keys=True),
            json.dumps(expected_result, sort_keys=True)
        )

    def test_asm_display_group_limit(self):
        self.assertRaises(ValueError, ASM, 1, list(range(26)))

    def test_disable_tracking(self):
        tracking_settings = TrackingSettings()
        tracking_settings.click_tracking = ClickTracking(False, False)

        self.assertEqual(
            tracking_settings.get(),
            {'click_tracking': {'enable': False, 'enable_text': False}}
        )

    def test_directly_setting_substitutions(self):
        personalization = Personalization()
        personalization.substitutions = [{'a': 0}]

    def test_from_emailmessage(self):
        message = EmailMessage()
        body = 'message that is not urgent'
        try:
            message.set_content(body)
        except AttributeError:
            # Python2
            message.set_payload(body)
        message.set_default_type('text/plain')
        message['Subject'] = 'URGENT TITLE'
        message['From'] = 'test@example.com'
        message['To'] = 'test@sendgrid.com'
        mail = Mail.from_EmailMessage(message)
        self.assertEqual(mail.subject.get(), 'URGENT TITLE')
        self.assertEqual(mail.from_email.email, 'test@example.com')
        self.assertEqual(len(mail.personalizations), 1)
        self.assertEqual(len(mail.personalizations[0].tos), 1)
        self.assertEqual(mail.personalizations[0].tos[0], {'email': 'test@sendgrid.com'})
        self.assertEqual(len(mail.contents), 1)
        content = mail.contents[0]
        self.assertEqual(content.type, 'text/plain')
        self.assertEqual(content.value, 'message that is not urgent')
