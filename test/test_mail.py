import sendgrid
import json
from sendgrid.helpers.mail import *
from sendgrid.version import __version__
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class UnitTests(unittest.TestCase):

    def test_helloEmail(self):
        self.maxDiff = None

        """Minimum required to send an email"""
        mail = Mail()

        mail.set_from(Email("test@example.com"))

        mail.set_subject("Hello World from the SendGrid Python Library")

        personalization = Personalization()
        personalization.add_to(Email("test@example.com"))
        mail.add_personalization(personalization)

        mail.add_content(Content("text/plain", "some text here"))
        mail.add_content(Content("text/html", "<html><body>some text here</body></html>"))

        self.assertEqual(json.dumps(mail.get(), sort_keys=True), '{"content": [{"type": "text/plain", "value": "some text here"}, {"type": "text/html", "value": "<html><body>some text here</body></html>"}], "from": {"email": "test@example.com"}, "personalizations": [{"to": [{"email": "test@example.com"}]}], "subject": "Hello World from the SendGrid Python Library"}')

    def test_kitchenSink(self):
        self.maxDiff = None

        """All settings set"""
        mail = Mail()

        mail.set_from(Email("test@example.com", "Example User"))

        mail.set_subject("Hello World from the SendGrid Python Library")

        personalization = Personalization()
        personalization.add_to(Email("test@example.com", "Example User"))
        personalization.add_to(Email("test@example.com", "Example User"))
        personalization.add_cc(Email("test@example.com", "Example User"))
        personalization.add_cc(Email("test@example.com", "Example User"))
        personalization.add_bcc(Email("test@example.com"))
        personalization.add_bcc(Email("test@example.com"))
        personalization.set_subject("Hello World from the Personalized SendGrid Python Library")
        personalization.add_header(Header("X-Test", "test"))
        personalization.add_header(Header("X-Mock", "true"))
        personalization.add_substitution(Substitution("%name%", "Example User"))
        personalization.add_substitution(Substitution("%city%", "Denver"))
        personalization.add_custom_arg(CustomArg("user_id", "343"))
        personalization.add_custom_arg(CustomArg("type", "marketing"))
        personalization.set_send_at(1443636843)
        mail.add_personalization(personalization)

        personalization2 = Personalization()
        personalization2.add_to(Email("test@example.com", "Example User"))
        personalization2.add_to(Email("test@example.com", "Example User"))
        personalization2.add_cc(Email("test@example.com", "Example User"))
        personalization2.add_cc(Email("test@example.com", "Example User"))
        personalization2.add_bcc(Email("test@example.com"))
        personalization2.add_bcc(Email("test@example.com"))
        personalization2.set_subject("Hello World from the Personalized SendGrid Python Library")
        personalization2.add_header(Header("X-Test", "test"))
        personalization2.add_header(Header("X-Mock", "true"))
        personalization2.add_substitution(Substitution("%name%", "Example User"))
        personalization2.add_substitution(Substitution("%city%", "Denver"))
        personalization2.add_custom_arg(CustomArg("user_id", "343"))
        personalization2.add_custom_arg(CustomArg("type", "marketing"))
        personalization2.set_send_at(1443636843)
        mail.add_personalization(personalization2)

        mail.add_content(Content("text/plain", "some text here"))
        mail.add_content(Content("text/html", "<html><body>some text here</body></html>"))

        attachment = Attachment()
        attachment.set_content("TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gQ3JhcyBwdW12")
        attachment.set_type("application/pdf")
        attachment.set_filename("balance_001.pdf")
        attachment.set_disposition("attachment")
        attachment.set_content_id("Balance Sheet")
        mail.add_attachment(attachment)

        attachment2 = Attachment()
        attachment2.set_content("BwdW")
        attachment2.set_type("image/png")
        attachment2.set_filename("banner.png")
        attachment2.set_disposition("inline")
        attachment2.set_content_id("Banner")
        mail.add_attachment(attachment2)

        mail.set_template_id("13b8f94f-bcae-4ec6-b752-70d6cb59f932")

        mail.add_section(Section("%section1%", "Substitution Text for Section 1"))
        mail.add_section(Section("%section2%", "Substitution Text for Section 2"))

        mail.add_header(Header("X-Test1", "test1"))
        mail.add_header(Header("X-Test3", "test2"))

        mail.add_category(Category("May"))
        mail.add_category(Category("2016"))

        mail.add_custom_arg(CustomArg("campaign", "welcome"))
        mail.add_custom_arg(CustomArg("weekday", "morning"))

        mail.set_send_at(1443636842)

        mail.set_batch_id("sendgrid_batch_id")

        mail.set_asm(ASM(99, [4, 5, 6, 7, 8]))

        mail.set_ip_pool_name("24")

        mail_settings = MailSettings()
        mail_settings.set_bcc_settings(BCCSettings(True, Email("test@example.com")))
        mail_settings.set_bypass_list_management(BypassListManagement(True))
        mail_settings.set_footer_settings(FooterSettings(True, "Footer Text", "<html><body>Footer Text</body></html>"))
        mail_settings.set_sandbox_mode(SandBoxMode(True))
        mail_settings.set_spam_check(SpamCheck(True, 1, "https://spamcatcher.sendgrid.com"))
        mail.set_mail_settings(mail_settings)

        tracking_settings = TrackingSettings()
        tracking_settings.set_click_tracking(ClickTracking(True, True))
        tracking_settings.set_open_tracking(OpenTracking(True, "Optional tag to replace with the open image in the body of the message"))
        tracking_settings.set_subscription_tracking(SubscriptionTracking(True, "text to insert into the text/plain portion of the message", "<html><body>html to insert into the text/html portion of the message</body></html>", "Optional tag to replace with the open image in the body of the message"))
        tracking_settings.set_ganalytics(Ganalytics(True, "some source", "some medium", "some term", "some content", "some campaign"))
        mail.set_tracking_settings(tracking_settings)

        mail.set_reply_to(Email("test@example.com"))

        self.assertEqual(json.dumps(mail.get(), sort_keys=True), '{"asm": {"group_id": 99, "groups_to_display": [4, 5, 6, 7, 8]}, "attachments": [{"content": "TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gQ3JhcyBwdW12", "content_id": "Balance Sheet", "disposition": "attachment", "filename": "balance_001.pdf", "type": "application/pdf"}, {"content": "BwdW", "content_id": "Banner", "disposition": "inline", "filename": "banner.png", "type": "image/png"}], "batch_id": "sendgrid_batch_id", "categories": ["May", "2016"], "content": [{"type": "text/plain", "value": "some text here"}, {"type": "text/html", "value": "<html><body>some text here</body></html>"}], "custom_args": {"campaign": "welcome", "weekday": "morning"}, "from": {"email": "test@example.com", "name": "Example User"}, "headers": {"X-Test1": "test1", "X-Test3": "test2"}, "ip_pool_name": "24", "mail_settings": {"bcc": {"email": "test@example.com", "enable": true}, "bypass_list_management": {"enable": true}, "footer": {"enable": true, "html": "<html><body>Footer Text</body></html>", "text": "Footer Text"}, "sandbox_mode": {"enable": true}, "spam_check": {"enable": true, "post_to_url": "https://spamcatcher.sendgrid.com", "threshold": 1}}, "personalizations": [{"bcc": [{"email": "test@example.com"}, {"email": "test@example.com"}], "cc": [{"email": "test@example.com", "name": "Example User"}, {"email": "test@example.com", "name": "Example User"}], "custom_args": {"type": "marketing", "user_id": "343"}, "headers": {"X-Mock": "true", "X-Test": "test"}, "send_at": 1443636843, "subject": "Hello World from the Personalized SendGrid Python Library", "substitutions": {"%city%": "Denver", "%name%": "Example User"}, "to": [{"email": "test@example.com", "name": "Example User"}, {"email": "test@example.com", "name": "Example User"}]}, {"bcc": [{"email": "test@example.com"}, {"email": "test@example.com"}], "cc": [{"email": "test@example.com", "name": "Example User"}, {"email": "test@example.com", "name": "Example User"}], "custom_args": {"type": "marketing", "user_id": "343"}, "headers": {"X-Mock": "true", "X-Test": "test"}, "send_at": 1443636843, "subject": "Hello World from the Personalized SendGrid Python Library", "substitutions": {"%city%": "Denver", "%name%": "Example User"}, "to": [{"email": "test@example.com", "name": "Example User"}, {"email": "test@example.com", "name": "Example User"}]}], "reply_to": {"email": "test@example.com"}, "sections": {"%section1%": "Substitution Text for Section 1", "%section2%": "Substitution Text for Section 2"}, "send_at": 1443636842, "subject": "Hello World from the SendGrid Python Library", "template_id": "13b8f94f-bcae-4ec6-b752-70d6cb59f932", "tracking_settings": {"click_tracking": {"enable": true, "enable_text": true}, "ganalytics": {"enable": true, "utm_campaign": "some campaign", "utm_content": "some content", "utm_medium": "some medium", "utm_source": "some source", "utm_term": "some term"}, "open_tracking": {"enable": true, "substitution_tag": "Optional tag to replace with the open image in the body of the message"}, "subscription_tracking": {"enable": true, "html": "<html><body>html to insert into the text/html portion of the message</body></html>", "substitution_tag": "Optional tag to replace with the open image in the body of the message", "text": "text to insert into the text/plain portion of the message"}}}')
