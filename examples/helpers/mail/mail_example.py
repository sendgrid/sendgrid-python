import json
import os
import urllib2
from sendgrid.helpers.mail import *
from sendgrid import *

# NOTE: you will need move this file to the root
# directory of this project to execute properly.


def build_hello_email():
    """Minimum required to send an email"""
    from_email = Email("test@example.com")
    subject = "Hello World from the SendGrid Python Library"
    to_email = Email("test@example.com")
    content = Content("text/plain", "some text here")
    mail = Mail(from_email, subject, to_email, content)
    mail.personalizations[0].add_to(Email("test2@example.com"))

    return mail.get()


def build_personalization(personalization):
    """Build personalization mock instance from a mock dict"""
    mock_personalization = Personalization()
    for to_addr in personalization['to_list']:
        mock_personalization.add_to(to_addr)

    for cc_addr in personalization['cc_list']:
        mock_personalization.add_to(cc_addr)

    for bcc_addr in personalization['bcc_list']:
        mock_personalization.add_bcc(bcc_addr)

    for header in personalization['headers']:
        mock_personalization.add_header(header)

    for substitution in personalization['substitutions']:
        mock_personalization.add_substitution(substitution)

    for arg in personalization['custom_args']:
        mock_personalization.add_custom_arg(arg)

    mock_personalization.subject = personalization['subject']
    mock_personalization.send_at = personalization['send_at']
    return mock_personalization


def get_mock_personalization_dict():
    """Get a dict of personalization mock."""
    mock_pers = dict()

    mock_pers['to_list'] = [Email("test1@example.com",
                                  "Example User"),
                            Email("test2@example.com",
                                  "Example User")]

    mock_pers['cc_list'] = [Email("test3@example.com",
                                  "Example User"),
                            Email("test4@example.com",
                                  "Example User")]

    mock_pers['bcc_list'] = [Email("test5@example.com"),
                             Email("test6@example.com")]

    mock_pers['subject'] = ("Hello World from the Personalized "
                            "SendGrid Python Library")

    mock_pers['headers'] = [Header("X-Test", "test"),
                            Header("X-Mock", "true")]

    mock_pers['substitutions'] = [Substitution("%name%", "Example User"),
                                  Substitution("%city%", "Denver")]

    mock_pers['custom_args'] = [CustomArg("user_id", "343"),
                                CustomArg("type", "marketing")]

    mock_pers['send_at'] = 1443636843
    return mock_pers


def build_attachment1():
    """Build attachment mock."""
    attachment = Attachment()
    attachment.content = ("TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNl"
                          "Y3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gQ3JhcyBwdW12")
    attachment.type = "application/pdf"
    attachment.filename = "balance_001.pdf"
    attachment.disposition = "attachment"
    attachment.content_id = "Balance Sheet"
    return attachment


def build_attachment2():
    """Build attachment mock."""
    attachment = Attachment()
    attachment.content = "BwdW"
    attachment.type = "image/png"
    attachment.filename = "banner.png"
    attachment.disposition = "inline"
    attachment.content_id = "Banner"
    return attachment


def build_mail_settings():
    """Build mail settings mock."""
    mail_settings = MailSettings()
    mail_settings.bcc_settings = BCCSettings(True, Email("test@example.com"))
    mail_settings.bypass_list_management = BypassListManagement(True)
    mail_settings.footer_settings = FooterSettings(True, "Footer Text",
                                                   ("<html><body>Footer "
                                                    "Text</body></html>"))
    mail_settings.sandbox_mode = SandBoxMode(True)
    mail_settings.spam_check = SpamCheck(True, 1,
                                         "https://spamcatcher.sendgrid.com")
    return mail_settings


def build_tracking_settings():
    """Build tracking settings mock."""
    tracking_settings = TrackingSettings()
    tracking_settings.click_tracking = ClickTracking(True, True)
    tracking_settings.open_tracking = OpenTracking(True,
                                                   ("Optional tag to "
                                                    "replace with the"
                                                    "open image in the "
                                                    "body of the message"))

    subs_track = SubscriptionTracking(True,
                                      ("text to insert into the "
                                       "text/plain portion of the"
                                       " message"),
                                      ("<html><body>html to insert "
                                       "into the text/html portion of "
                                       "the message</body></html>"),
                                      ("Optional tag to replace with "
                                       "the open image in the body of "
                                       "the message"))

    tracking_settings.subscription_tracking = subs_track
    tracking_settings.ganalytics = Ganalytics(True, "some source",
                                              "some medium", "some term",
                                              "some_content", "some_campaign")
    return tracking_settings


def build_kitchen_sink():
    """All settings set"""
    mail = Mail()

    mail.from_email = Email("test@example.com", "Example User")
    mail.subject = "Hello World from the SendGrid Python Library"

    personalization = get_mock_personalization_dict()
    mail.add_personalization(build_personalization(personalization))
    mail.add_personalization(build_personalization(personalization))

    mail.add_content(Content("text/plain", "some text here"))
    mail.add_content(Content("text/html", ("<html><body>some text "
                             "here</body></html>")))

    mail.add_attachment(build_attachment1())
    mail.add_attachment(build_attachment2())

    mail.template_id = "13b8f94f-bcae-4ec6-b752-70d6cb59f932"

    mail.add_section(Section("%section1%", "Substitution Text for Section 1"))
    mail.add_section(Section("%section2%", "Substitution Text for Section 2"))

    mail.add_header(Header("X-Test1", "test1"))
    mail.add_header(Header("X-Test3", "test2"))

    mail.add_category(Category("May"))
    mail.add_category(Category("2016"))

    mail.add_custom_arg(CustomArg("campaign", "welcome"))
    mail.add_custom_arg(CustomArg("weekday", "morning"))

    mail.send_at = 1443636842

    # This must be a valid [batch ID]
    # (https://sendgrid.com/docs/API_Reference/SMTP_API/scheduling_parameters.html) to work
    # mail.set_batch_id("N2VkYjBjYWItMGU4OC0xMWU2LWJhMzYtZjQ1Yzg5OTBkNzkxLWM5ZTUyZjNhOA")
    mail.asm = ASM(99, [4, 5, 6, 7, 8])
    mail.ip_pool_name = "24"
    mail.mail_settings = build_mail_settings()
    mail.tracking_settings = build_tracking_settings()
    mail.reply_to = Email("test@example.com")

    return mail.get()


def send_hello_email():
    # Assumes you set your environment variable:
    # https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment-variables-and-your-sendgrid-api-key
    sg = SendGridAPIClient()
    data = build_hello_email()
    response = sg.client.mail.send.post(request_body=data)
    print(response.status_code)
    print(response.headers)
    print(response.body)


def send_kitchen_sink():
    # Assumes you set your environment variable:
    # https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment-variables-and-your-sendgrid-api-key
    sg = SendGridAPIClient()
    data = build_kitchen_sink()
    response = sg.client.mail.send.post(request_body=data)
    print(response.status_code)
    print(response.headers)
    print(response.body)


# this will actually send an email
send_hello_email()

# this will only send an email if you set SandBox Mode to False
send_kitchen_sink()
