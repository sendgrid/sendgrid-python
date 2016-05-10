"""v3/mail/send response body builder"""
import json


class Mail(object):
    """Creates the response body for v3/mail/send"""
    def __init__(self, from_email = None, subject = None, to_email = None, content = None):
        self.from_email = None
        self.subject = None
        self.personalizations = None
        self.contents = None
        self.attachments = None
        self.template_id = None
        self.sections = None
        self.headers = None
        self.categories = None
        self.custom_args = None
        self.send_at = None
        self.batch_id = None
        self.asm = None
        self.ip_pool_name = None
        self.mail_settings = None
        self.tracking_settings = None
        self.reply_to = None

        # Minimum required to send an email
        if from_email and subject and to_email and content:
            self.set_from(from_email)
            personalization = Personalization()
            personalization.add_to(to_email)
            self.add_personalization(personalization)
            self.set_subject(subject)
            self.add_content(content)

    def __str__(self):
        self.get()

    def get(self):
        """
        :return: response body dict
        """
        mail = {}
        if self.from_email:
            mail["from"] = self.from_email.get()
        if self.subject:
            mail["subject"] = self.subject
        if self.personalizations:
            mail["personalizations"] = [personalization.get() for personalization in self.personalizations]
        if self.contents:
            mail["content"] = [ob.get() for ob in self.contents]
        if self.attachments:
            mail["attachments"] = [ob.get() for ob in self.attachments]
        if self.template_id:
            mail["template_id"] = self.template_id
        if self.sections:
            sections = {}
            for key in self.sections:
                sections.update(key.get())
            mail["sections"] = sections
        if self.headers:
            headers = {}
            for key in self.headers:
                headers.update(key.get())
            mail["headers"] = headers
        if self.categories:
            mail["categories"] = [category.get() for category in self.categories]
        if self.custom_args:
            custom_args = {}
            for key in self.custom_args:
                custom_args.update(key.get())
            mail["custom_args"] = custom_args
        if self.send_at:
            mail["send_at"] = self.send_at
        if self.batch_id:
            mail["batch_id"] = self.batch_id
        if self.asm:
            mail["asm"] = self.asm
        if self.ip_pool_name:
            mail["ip_pool_name"] = self.ip_pool_name
        if self.mail_settings:
            mail["mail_settings"] = self.mail_settings.get()
        if self.tracking_settings:
            mail["tracking_settings"] = self.tracking_settings.get()
        if self.reply_to:
            mail["reply_to"] = self.reply_to.get()
        return mail

    def set_from(self, email):
        self.from_email = email

    def set_subject(self, subject):
        self.subject = subject

    def add_personalization(self, personalizations):
        if self.personalizations is None:
            self.personalizations = []
        self.personalizations.append(personalizations)

    def add_content(self, content):
        if self.contents is None:
            self.contents = []
        self.contents.append(content)

    def add_attachment(self, attachment):
        if self.attachments is None:
            self.attachments = []
        self.attachments.append(attachment)

    def set_template_id(self, template_id):
        self.template_id = template_id

    def add_section(self, section):
        if self.sections is None:
            self.sections = []
        self.sections.append(section)

    def add_header(self, header):
        if self.headers is None:
            self.headers = []
        self.headers.append(header)

    def add_category(self, category):
        if self.categories is None:
            self.categories = []
        self.categories.append(category)

    def add_custom_arg(self, custom_arg):
        if self.custom_args is None:
            self.custom_args = []
        self.custom_args.append(custom_arg)

    def set_send_at(self, send_at):
        self.send_at = send_at

    def set_batch_id(self, batch_id):
        self.batch_id = batch_id

    def set_asm(self, asm):
        self.asm = asm.get()

    def set_mail_settings(self, mail_settings):
        self.mail_settings = mail_settings

    def set_tracking_settings(self, tracking_settings):
        self.tracking_settings = tracking_settings

    def set_ip_pool_name(self, ip_pool_name):
        self.ip_pool_name = ip_pool_name

    def set_reply_to(self, reply_to):
        self.reply_to = reply_to

################################################################
# The following objects are meant to be extended with validation
################################################################


class Email(object):
    def __init__(self, email=None, name=None):
        self.name = name if name else None
        self.email = email if email else None

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def get(self):
        email = {}
        if self.name:
            email["name"] = self.name
        if self.email:
            email["email"] = self.email
        return email


class Content(object):
    def __init__(self, type=None, value=None):
        self.type = type if type else None
        self.value = value if value else None

    def set_type(self, type):
        self.type = type

    def set_value(self, value):
        self.value = value

    def get(self):
        content = {}
        if self.type:
            content["type"] = self.type
        if self.value:
            content["value"] = self.value
        return content


class Header(object):
    def __init__(self, key=None, value=None):
        self.key = key if key else None
        self.value = value if value else None

    def set_key(self, key):
        self.key = key

    def set_value(self, value):
        self.value = value

    def get(self):
        header = {}
        if self.key and self.value:
            header[self.key] = self.value
        return header


class Substitution(object):
    def __init__(self, key=None, value=None):
        self.key = key if key else None
        self.value = value if value else None

    def set_key(self, key):
        self.key = key

    def set_value(self, value):
        self.value = value

    def get(self):
        substitution = {}
        if self.key and self.value:
            substitution[self.key] = self.value
        return substitution


class Section(object):
    def __init__(self, key=None, value=None):
        self.key = key if key else None
        self.value = value if value else None

    def set_key(self, key):
        self.key = key

    def set_value(self, value):
        self.value = value

    def get(self):
        section = {}
        if self.key and self.value:
            section[self.key] = self.value
        return section


class CustomArg(object):
    def __init__(self, key=None, value=None):
        self.key = key if key else None
        self.value = value if value else None

    def set_key(self, key):
        self.key = key

    def set_value(self, value):
        self.value = value

    def get(self):
        custom_arg = {}
        if self.key and self.value:
            custom_arg[self.key] = self.value
        return custom_arg


class Personalization(object):
    def __init__(self):
        self.tos = None
        self.ccs = None
        self.bccs = None
        self.subject = None
        self.headers = None
        self.substitutions = None
        self.custom_args = None
        self.send_at = None

    def add_to(self, email):
        if self.tos is None:
            self.tos = []
        self.tos.append(email.get())

    def add_cc(self, email):
        if self.ccs is None:
            self.ccs = []
        self.ccs.append(email.get())

    def add_bcc(self, email):
        if self.bccs is None:
            self.bccs = []
        self.bccs.append(email.get())

    def set_subject(self, subject):
        self.subject = subject

    def add_header(self, header):
        if self.headers is None:
            self.headers = []
        self.headers.append(header.get())

    def add_substitution(self, substitution):
        if self.substitutions is None:
            self.substitutions = []
        self.substitutions.append(substitution.get())

    def add_custom_arg(self, custom_arg):
        if self.custom_args is None:
            self.custom_args = []
        self.custom_args.append(custom_arg.get())

    def set_send_at(self, send_at):
        self.send_at = send_at

    def get(self):
        personalization = {}
        if self.tos:
            personalization["to"] = self.tos
        if self.ccs:
            personalization["cc"] = self.ccs
        if self.bccs:
            personalization["bcc"] = self.bccs
        if self.subject:
            personalization["subject"] = self.subject
        if self.headers:
            headers = {}
            for key in self.headers:
                headers.update(key)
            personalization["headers"] = headers
        if self.substitutions:
            substitutions = {}
            for key in self.substitutions:
                substitutions.update(key)
            personalization["substitutions"] = substitutions
        if self.custom_args:
            custom_args = {}
            for key in self.custom_args:
                custom_args.update(key)
            personalization["custom_args"] = custom_args
        if self.send_at:
            personalization["send_at"] = self.send_at
        return personalization


class Attachment(object):
    def __init__(self):
        self.content = None
        self.type = None
        self.filename = None
        self.disposition = None
        self.content_id = None

    def set_content(self, content):
        self.content = content

    def set_type(self, type):
        self.type = type

    def set_filename(self, filename):
        self.filename = filename

    def set_disposition(self, disposition):
        self.disposition = disposition

    def set_content_id(self, content_id):
        self.content_id = content_id

    def get(self):
        attachment = {}
        if self.content:
            attachment["content"] = self.content
        if self.type:
            attachment["type"] = self.type
        if self.filename:
            attachment["filename"] = self.filename
        if self.disposition:
            attachment["disposition"] = self.disposition
        if self.content_id:
            attachment["content_id"] = self.content_id
        return attachment


class Category(object):
    def __init__(self, name=None):
        self.name = name if name else None

    def get(self):
        return self.name


class ASM(object):
    def __init__(self, group_id=None, groups_to_display=None):
        self.group_id = group_id if group_id else None
        self.groups_to_display = groups_to_display if groups_to_display else None

    def get(self):
        asm = {}
        if self.group_id:
            asm["group_id"] = self.group_id
        if self.groups_to_display:
            asm["groups_to_display"] = self.groups_to_display
        return asm


class BCCSettings(object):
    def __init__(self, enable=None, email=None):
        self.enable = enable if enable else None
        self.email = email if email else None

    def get(self):
        bcc_settings = {}
        if self.enable:
            bcc_settings["enable"] = self.enable
        if self.email:
            email = self.email.get()
            bcc_settings["email"] = email["email"]
        return bcc_settings


class BypassListManagement(object):
    def __init__(self, enable=None):
        self.enable = enable if enable else None

    def get(self):
        bypass_list_management = {}
        bypass_list_management["enable"] = self.enable
        return bypass_list_management


class FooterSettings(object):
    def __init__(self, enable=None, text=None, html=None):
        self.enable = enable if enable else None
        self.text = text if text else text
        self.html = html if html else html

    def set_enable(self, enable):
        self.enable = enable

    def set_text(self, text):
        self.text = text

    def set_html(self, html):
        self.html = html

    def get(self):
        footer_settings = {}
        if self.enable:
            footer_settings["enable"] = self.enable
        if self.text:
            footer_settings["text"] = self.text
        if self.html:
            footer_settings["html"] = self.html
        return footer_settings


class SandBoxMode(object):
    def __init__(self, enable=None):
        self.enable = enable if enable else False

    def get(self):
        sandbox_mode = {}
        sandbox_mode["enable"] = self.enable
        return sandbox_mode


class SpamCheck(object):
    def __init__(self, enable=None, threshold=None, post_to_url=None):
        self.enable = enable if enable else None
        self.threshold = threshold if threshold else None
        self.post_to_url = post_to_url if post_to_url else None

    def set_enable(self, enable):
        self.enable = enable

    def set_threshold(self, threshold):
        self.threshold = threshold

    def set_post_to_url(self, post_to_url):
        self.post_to_url = post_to_url

    def get(self):
        spam_check = {}
        if self.enable:
            spam_check["enable"] = self.enable
        if self.threshold:
            spam_check["threshold"] = self.threshold
        if self.post_to_url:
            spam_check["post_to_url"] = self.post_to_url
        return spam_check


class MailSettings(object):
    def __init__(self):
        self.bcc_settings = None
        self.bypass_list_management = None
        self.footer_settings = None
        self.sandbox_mode = None
        self.spam_check = None

    def set_bcc_settings(self, bcc_settings):
        self.bcc_settings = bcc_settings

    def set_bypass_list_management(self, bypass_list_management):
        self.bypass_list_management = bypass_list_management

    def set_footer_settings(self, footer_settings):
        self.footer_settings = footer_settings

    def set_sandbox_mode(self, sandbox_mode):
        self.sandbox_mode = sandbox_mode

    def set_spam_check(self, spam_check):
        self.spam_check = spam_check

    def get(self):
        mail_settings = {}
        if self.bcc_settings:
            mail_settings["bcc"] = self.bcc_settings.get()
        if self.bypass_list_management:
            mail_settings["bypass_list_management"] = self.bypass_list_management.get()
        if self.footer_settings:
            mail_settings["footer"] = self.footer_settings.get()
        if self.sandbox_mode:
            mail_settings["sandbox_mode"] = self.sandbox_mode.get()
        if self.spam_check:
            mail_settings["spam_check"] = self.spam_check.get()
        return mail_settings


class ClickTracking(object):
    def __init__(self, enable=None, enable_text=None):
        self.enable = enable if enable else None
        self.enable_text = enable_text if enable_text else None

    def set_enable(self, enable):
        self.enable = enable

    def set_enable_text(self, enable_text):
        self.enable_text = enable_text

    def get(self):
        click_tracking = {}
        if self.enable:
            click_tracking["enable"] = self.enable
        if self.enable_text:
            click_tracking["enable_text"] = self.enable_text
        return click_tracking


class OpenTracking(object):
    def __init__(self, enable=None, substitution_tag=None):
        self.enable = enable if enable else None
        self.substitution_tag = substitution_tag if substitution_tag else None

    def set_enable(self, enable):
        self.enable = enable

    def set_substitution_tag(self, substitution_tag):
        self.substitution_tag = substitution_tag

    def get(self):
        open_tracking = {}
        if self.enable:
            open_tracking["enable"] = self.enable
        if self.substitution_tag:
            open_tracking["substitution_tag"] = self.substitution_tag
        return open_tracking


class SubscriptionTracking(object):
    def __init__(self, enable=None, text=None, html=None, substitution_tag=None):
        self.enable = enable if enable else None
        self.text = text if text else None
        self.html = html if html else None
        self.substitution_tag = substitution_tag if substitution_tag else None

    def set_enable(self, enable):
        self.enable = enable

    def set_text(self, text):
        self.text = text

    def set_html(self, html):
        self.html = html

    def set_substitution_tag(self, substitution_tag):
        self.substitution_tag = substitution_tag

    def get(self):
        subscription_tracking = {}
        if self.enable:
            subscription_tracking["enable"] = self.enable
        if self.text:
            subscription_tracking["text"] = self.text
        if self.html:
            subscription_tracking["html"] = self.html
        if self.substitution_tag:
            subscription_tracking["substitution_tag"] = self.substitution_tag
        return subscription_tracking


class Ganalytics(object):
    def __init__(self,
                 enable=None,
                 utm_source=None,
                 utm_medium=None,
                 utm_term=None,
                 utm_content=None,
                 utm_campaign=None):
        self.enable = enable if enable else None
        self.utm_source = utm_source if utm_source else None
        self.utm_medium = utm_medium if utm_medium else None
        self.utm_term = utm_term if utm_term else None
        self.utm_content = utm_content if utm_content else None
        self.utm_campaign = utm_campaign if utm_campaign else None

    def set_enable(self, enable):
        self.enable = enable

    def set_utm_source(self, utm_source):
        self.utm_source = utm_source

    def set_utm_medium(self, utm_medium):
        self.utm_medium = utm_medium

    def set_utm_term(self, utm_term):
        self.utm_term = utm_term

    def set_utm_content(self, utm_content):
        self.utm_content = utm_content

    def set_utm_campaign(self, utm_campaign):
        self.utm_campaign = utm_campaign

    def get(self):
        ganalytics = {}
        if self.enable:
            ganalytics["enable"] = self.enable
        if self.utm_source:
            ganalytics["utm_source"] = self.utm_source
        if self.utm_medium:
            ganalytics["utm_medium"] = self.utm_medium
        if self.utm_term:
            ganalytics["utm_term"] = self.utm_term
        if self.utm_content:
            ganalytics["utm_content"] = self.utm_content
        if self.utm_campaign:
            ganalytics["utm_campaign"] = self.utm_campaign
        return ganalytics


class TrackingSettings(object):
    def __init__(self):
        self.click_tracking = None
        self.open_tracking = None
        self.subscription_tracking = None
        self.ganalytics = None

    def set_click_tracking(self, click_tracking):
        self.click_tracking = click_tracking

    def set_open_tracking(self, open_tracking):
        self.open_tracking = open_tracking

    def set_subscription_tracking(self, subscription_tracking):
        self.subscription_tracking = subscription_tracking

    def set_ganalytics(self, ganalytics):
        self.ganalytics = ganalytics

    def get(self):
        tracking_settings = {}
        if self.click_tracking:
            tracking_settings["click_tracking"] = self.click_tracking.get()
        if self.open_tracking:
            tracking_settings["open_tracking"] = self.open_tracking.get()
        if self.subscription_tracking:
            tracking_settings["subscription_tracking"] = self.subscription_tracking.get()
        if self.ganalytics:
            tracking_settings["ganalytics"] = self.ganalytics.get()
        return tracking_settings
