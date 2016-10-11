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
        if self.from_email != None:
            mail["from"] = self.from_email.get()
        if self.subject != None:
            mail["subject"] = self.subject
        if self.personalizations != None:
            mail["personalizations"] = [personalization.get() for personalization in self.personalizations]
        if self.contents != None:
            mail["content"] = [ob.get() for ob in self.contents]
        if self.attachments != None:
            mail["attachments"] = [ob.get() for ob in self.attachments]
        if self.template_id != None:
            mail["template_id"] = self.template_id
        if self.sections != None:
            sections = {}
            for key in self.sections:
                sections.update(key.get())
            mail["sections"] = sections
        if self.headers != None:
            headers = {}
            for key in self.headers:
                headers.update(key.get())
            mail["headers"] = headers
        if self.categories != None:
            mail["categories"] = [category.get() for category in self.categories]
        if self.custom_args != None:
            custom_args = {}
            for key in self.custom_args:
                custom_args.update(key.get())
            mail["custom_args"] = custom_args
        if self.send_at != None:
            mail["send_at"] = self.send_at
        if self.batch_id != None:
            mail["batch_id"] = self.batch_id
        if self.asm != None:
            mail["asm"] = self.asm
        if self.ip_pool_name != None:
            mail["ip_pool_name"] = self.ip_pool_name
        if self.mail_settings != None:
            mail["mail_settings"] = self.mail_settings.get()
        if self.tracking_settings != None:
            mail["tracking_settings"] = self.tracking_settings.get()
        if self.reply_to != None:
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
        if isinstance(header, dict):
            (k,v) = list(header.items())[0]
            self.headers.append(Header(k,v))
        else:
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
        self.name = name if name != None else None
        self.email = email if email != None else None

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def get(self):
        email = {}
        if self.name != None:
            email["name"] = self.name
        if self.email != None:
            email["email"] = self.email
        return email


class Content(object):
    def __init__(self, type=None, value=None):
        self.type = type if type != None else None
        self.value = value if value != None else None

    def set_type(self, type):
        self.type = type

    def set_value(self, value):
        self.value = value

    def get(self):
        content = {}
        if self.type != None:
            content["type"] = self.type
        if self.value != None:
            content["value"] = self.value
        return content


class Header(object):
    def __init__(self, key=None, value=None):
        self.key = key if key != None else None
        self.value = value if value != None else None

    def set_key(self, key):
        self.key = key

    def set_value(self, value):
        self.value = value

    def get(self):
        header = {}
        if self.key != None and self.value != None:
            header[self.key] = self.value
        return header


class Substitution(object):
    def __init__(self, key=None, value=None):
        self.key = key if key != None else None
        self.value = value if value != None else None

    def set_key(self, key):
        self.key = key

    def set_value(self, value):
        self.value = value

    def get(self):
        substitution = {}
        if self.key != None and self.value != None:
            substitution[self.key] = self.value
        return substitution


class Section(object):
    def __init__(self, key=None, value=None):
        self.key = key if key != None else None
        self.value = value if value != None else None

    def set_key(self, key):
        self.key = key

    def set_value(self, value):
        self.value = value

    def get(self):
        section = {}
        if self.key != None and self.value != None:
            section[self.key] = self.value
        return section


class CustomArg(object):
    def __init__(self, key=None, value=None):
        self.key = key if key != None else None
        self.value = value if value != None else None

    def set_key(self, key):
        self.key = key

    def set_value(self, value):
        self.value = value

    def get(self):
        custom_arg = {}
        if self.key != None and self.value != None:
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
        if self.tos != None:
            personalization["to"] = self.tos
        if self.ccs != None:
            personalization["cc"] = self.ccs
        if self.bccs != None:
            personalization["bcc"] = self.bccs
        if self.subject != None:
            personalization["subject"] = self.subject
        if self.headers != None:
            headers = {}
            for key in self.headers:
                headers.update(key)
            personalization["headers"] = headers
        if self.substitutions != None:
            substitutions = {}
            for key in self.substitutions:
                substitutions.update(key)
            personalization["substitutions"] = substitutions
        if self.custom_args != None:
            custom_args = {}
            for key in self.custom_args:
                custom_args.update(key)
            personalization["custom_args"] = custom_args
        if self.send_at != None:
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
        if self.content != None:
            attachment["content"] = self.content
        if self.type != None:
            attachment["type"] = self.type
        if self.filename != None:
            attachment["filename"] = self.filename
        if self.disposition != None:
            attachment["disposition"] = self.disposition
        if self.content_id != None:
            attachment["content_id"] = self.content_id
        return attachment


class Category(object):
    def __init__(self, name=None):
        self.name = name if name != None else None

    def get(self):
        return self.name


class ASM(object):
    def __init__(self, group_id=None, groups_to_display=None):
        self.group_id = group_id if group_id != None else None
        self.groups_to_display = groups_to_display if groups_to_display != None else None

    def get(self):
        asm = {}
        if self.group_id != None:
            asm["group_id"] = self.group_id
        if self.groups_to_display != None:
            asm["groups_to_display"] = self.groups_to_display
        return asm


class BCCSettings(object):
    def __init__(self, enable=None, email=None):
        self.enable = enable if enable != None else None
        self.email = email if email != None else None

    def get(self):
        bcc_settings = {}
        if self.enable != None:
            bcc_settings["enable"] = self.enable
        if self.email != None:
            email = self.email.get()
            bcc_settings["email"] = email["email"]
        return bcc_settings


class BypassListManagement(object):
    def __init__(self, enable=None):
        self.enable = enable if enable != None else None

    def get(self):
        bypass_list_management = {}
        if self.enable != None:
            bypass_list_management["enable"] = self.enable
        return bypass_list_management


class FooterSettings(object):
    def __init__(self, enable=None, text=None, html=None):
        self.enable = enable if enable != None else None
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
        if self.enable != None:
            footer_settings["enable"] = self.enable
        if self.text != None:
            footer_settings["text"] = self.text
        if self.html != None:
            footer_settings["html"] = self.html
        return footer_settings


class SandBoxMode(object):
    def __init__(self, enable=None):
        self.enable = enable if enable else False

    def get(self):
        sandbox_mode = {}
        if self.enable != None:
            sandbox_mode["enable"] = self.enable
        return sandbox_mode


class SpamCheck(object):
    def __init__(self, enable=None, threshold=None, post_to_url=None):
        self.enable = enable if enable != None else None
        self.threshold = threshold if threshold != None else None
        self.post_to_url = post_to_url if post_to_url != None else None

    def set_enable(self, enable):
        self.enable = enable

    def set_threshold(self, threshold):
        self.threshold = threshold

    def set_post_to_url(self, post_to_url):
        self.post_to_url = post_to_url

    def get(self):
        spam_check = {}
        if self.enable != None:
            spam_check["enable"] = self.enable
        if self.threshold != None:
            spam_check["threshold"] = self.threshold
        if self.post_to_url != None:
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
        if self.bcc_settings != None:
            mail_settings["bcc"] = self.bcc_settings.get()
        if self.bypass_list_management != None:
            mail_settings["bypass_list_management"] = self.bypass_list_management.get()
        if self.footer_settings != None:
            mail_settings["footer"] = self.footer_settings.get()
        if self.sandbox_mode != None:
            mail_settings["sandbox_mode"] = self.sandbox_mode.get()
        if self.spam_check != None:
            mail_settings["spam_check"] = self.spam_check.get()
        return mail_settings


class ClickTracking(object):
    def __init__(self, enable=None, enable_text=None):
        self.enable = enable if enable else None
        self.enable_text = enable_text if enable_text !=None else None

    def set_enable(self, enable):
        self.enable = enable

    def set_enable_text(self, enable_text):
        self.enable_text = enable_text

    def get(self):
        click_tracking = {}
        if self.enable != None:
            click_tracking["enable"] = self.enable
        if self.enable_text != None:
            click_tracking["enable_text"] = self.enable_text
        return click_tracking


class OpenTracking(object):
    def __init__(self, enable=None, substitution_tag=None):
        self.enable = enable if enable != None else None
        self.substitution_tag = substitution_tag if substitution_tag !=None else None

    def set_enable(self, enable):
        self.enable = enable

    def set_substitution_tag(self, substitution_tag):
        self.substitution_tag = substitution_tag

    def get(self):
        open_tracking = {}
        if self.enable != None:
            open_tracking["enable"] = self.enable
        if self.substitution_tag != None:
            open_tracking["substitution_tag"] = self.substitution_tag
        return open_tracking


class SubscriptionTracking(object):
    def __init__(self, enable=None, text=None, html=None, substitution_tag=None):
        self.enable = enable if enable != None else None
        self.text = text if text != None else None
        self.html = html if html != None else None
        self.substitution_tag = substitution_tag if substitution_tag != None else None

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
        if self.enable != None:
            subscription_tracking["enable"] = self.enable
        if self.text != None:
            subscription_tracking["text"] = self.text
        if self.html != None:
            subscription_tracking["html"] = self.html
        if self.substitution_tag != None:
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
        self.enable = enable if enable != None else None
        self.utm_source = utm_source if utm_source != None else None
        self.utm_medium = utm_medium if utm_medium != None else None
        self.utm_term = utm_term if utm_term != None else None
        self.utm_content = utm_content if utm_content != None else None
        self.utm_campaign = utm_campaign if utm_campaign != None else None

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
        if self.enable != None:
            ganalytics["enable"] = self.enable
        if self.utm_source != None:
            ganalytics["utm_source"] = self.utm_source
        if self.utm_medium != None:
            ganalytics["utm_medium"] = self.utm_medium
        if self.utm_term != None:
            ganalytics["utm_term"] = self.utm_term
        if self.utm_content != None:
            ganalytics["utm_content"] = self.utm_content
        if self.utm_campaign != None:
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
        if self.click_tracking != None:
            tracking_settings["click_tracking"] = self.click_tracking.get()
        if self.open_tracking != None:
            tracking_settings["open_tracking"] = self.open_tracking.get()
        if self.subscription_tracking != None:
            tracking_settings["subscription_tracking"] = self.subscription_tracking.get()
        if self.ganalytics != None:
            tracking_settings["ganalytics"] = self.ganalytics.get()
        return tracking_settings
