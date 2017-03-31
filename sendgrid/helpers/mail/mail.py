"""v3/mail/send response body builder"""


class Mail(object):
    """Creates the response body for v3/mail/send"""
    def __init__(
            self, from_email=None, subject=None, to_email=None, content=None):
        self._from_email = None
        self._subject = None
        self._template_id = None
        self._send_at = None
        self._batch_id = None
        self._asm = None
        self._ip_pool_name = None
        self._mail_settings = None
        self._tracking_settings = None
        self._reply_to = None
        self._personalizations = None
        self._contents = None
        self._attachments = None
        self._sections = None
        self._headers = None
        self._categories = None
        self._custom_args = None

        # Minimum required to send an email
        if from_email and subject and to_email and content:
            self.from_email = from_email
            self.subject = subject
            personalization = Personalization()
            personalization.add_to(to_email)
            self.add_personalization(personalization)
            self.add_content(content)

    def __str__(self):
        self.get()

    def get(self):
        """
        :return: response body dict
        """
        mail = {}
        if self.from_email is not None:
            mail["from"] = self.from_email.get()
        if self.subject is not None:
            mail["subject"] = self.subject

        if self.personalizations is not None:
            mail["personalizations"] = [
                personalization.get()
                for personalization in self.personalizations
            ]

        if self.contents is not None:
            mail["content"] = [ob.get() for ob in self.contents]

        if self.attachments is not None:
            mail["attachments"] = [ob.get() for ob in self.attachments]

        if self.template_id is not None:
            mail["template_id"] = self.template_id

        if self.sections is not None:
            sections = {}
            for key in self.sections:
                sections.update(key.get())
            mail["sections"] = sections

        if self.headers is not None:
            headers = {}
            for key in self.headers:
                headers.update(key.get())
            mail["headers"] = headers

        if self.categories is not None:
            mail["categories"] = [category.get() for category in
                                  self.categories]

        if self.custom_args is not None:
            custom_args = {}
            for key in self.custom_args:
                custom_args.update(key.get())
            mail["custom_args"] = custom_args

        if self.send_at is not None:
            mail["send_at"] = self.send_at

        if self.batch_id is not None:
            mail["batch_id"] = self.batch_id

        if self.asm is not None:
            mail["asm"] = self.asm.get()

        if self.ip_pool_name is not None:
            mail["ip_pool_name"] = self.ip_pool_name

        if self.mail_settings is not None:
            mail["mail_settings"] = self.mail_settings.get()

        if self.tracking_settings is not None:
            mail["tracking_settings"] = self.tracking_settings.get()

        if self.reply_to is not None:
            mail["reply_to"] = self.reply_to.get()
        return mail

    @property
    def from_email(self):
        return self._from_email

    @from_email.setter
    def from_email(self, value):
        self._from_email = value

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value

    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value

    @property
    def send_at(self):
        return self._send_at

    @send_at.setter
    def send_at(self, value):
        self._send_at = value

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value

    @property
    def asm(self):
        return self._asm

    @asm.setter
    def asm(self, value):
        self._asm = value

    @property
    def mail_settings(self):
        return self._mail_settings

    @mail_settings.setter
    def mail_settings(self, value):
        self._mail_settings = value

    @property
    def tracking_settings(self):
        return self._tracking_settings

    @tracking_settings.setter
    def tracking_settings(self, value):
        self._tracking_settings = value

    @property
    def ip_pool_name(self):
        return self._ip_pool_name

    @ip_pool_name.setter
    def ip_pool_name(self, value):
        self._ip_pool_name = value

    @property
    def reply_to(self):
        return self._reply_to

    @reply_to.setter
    def reply_to(self, value):
        self._reply_to = value

    @property
    def personalizations(self):
        return self._personalizations

    def add_personalization(self, personalizations):
        if self._personalizations is None:
            self._personalizations = []
        self._personalizations.append(personalizations)

    @property
    def contents(self):
        return self._contents

    def add_content(self, content):
        if self._contents is None:
            self._contents = []
        self._contents.append(content)

    @property
    def attachments(self):
        return self._attachments

    def add_attachment(self, attachment):
        if self._attachments is None:
            self._attachments = []
        self._attachments.append(attachment)

    @property
    def sections(self):
        return self._sections

    def add_section(self, section):
        if self._sections is None:
            self._sections = []
        self._sections.append(section)

    @property
    def headers(self):
        return self._headers

    def add_header(self, header):
        if self._headers is None:
            self._headers = []
        if isinstance(header, dict):
            (k, v) = list(header.items())[0]
            self._headers.append(Header(k, v))
        else:
            self._headers.append(header)

    @property
    def categories(self):
        return self._categories

    def add_category(self, category):
        if self._categories is None:
            self._categories = []
        self._categories.append(category)

    @property
    def custom_args(self):
        return self._custom_args

    def add_custom_arg(self, custom_arg):
        if self._custom_args is None:
            self._custom_args = []
        self._custom_args.append(custom_arg)


################################################################
# The following objects are meant to be extended with validation
################################################################


class Email(object):

    def __init__(self, email=None, name=None):
        self._name = None
        self._email = None

        if email is not None:
            self.email = email
        if name is not None:
            self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    def get(self):
        email = {}
        if self.name is not None:
            email["name"] = self.name

        if self.email is not None:
            email["email"] = self.email
        return email


class Content(object):

    def __init__(self, type_=None, value=None):
        self._type = None
        self._value = None

        if type_ is not None:
            self.type = type_

        if value is not None:
            self.value = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def get(self):
        content = {}
        if self.type is not None:
            content["type"] = self.type

        if self.value is not None:
            content["value"] = self.value
        return content


class Header(object):

    def __init__(self, key=None, value=None):
        self._key = None
        self._value = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def get(self):
        header = {}
        if self.key is not None and self.value is not None:
            header[self.key] = self.value
        return header


class Substitution(object):

    def __init__(self, key=None, value=None):
        self._key = None
        self._value = None

        if key is not None:
            self.key = key

        if value is not None:
            self.value = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = str(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = str(value)

    def get(self):
        substitution = {}
        if self.key is not None and self.value is not None:
            substitution[self.key] = self.value
        return substitution


class Section(object):

    def __init__(self, key=None, value=None):
        self._key = None
        self._value = None

        if key is not None:
            self.key = key

        if value is not None:
            self.value = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def get(self):
        section = {}
        if self.key is not None and self.value is not None:
            section[self.key] = self.value
        return section


class CustomArg(object):

    def __init__(self, key=None, value=None):
        self._key = None
        self._value = None

        if key is not None:
            self.key = key

        if value is not None:
            self.value = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def get(self):
        custom_arg = {}
        if self.key is not None and self.value is not None:
            custom_arg[self.key] = self.value
        return custom_arg


class Personalization(object):

    def __init__(self):
        self._tos = None
        self._ccs = None
        self._bccs = None
        self._subject = None
        self._headers = None
        self._substitutions = None
        self._custom_args = None
        self._send_at = None

    @property
    def tos(self):
        return self._tos

    @tos.setter
    def tos(self, value):
        self._tos = value

    def add_to(self, email):
        if self._tos is None:
            self._tos = []
        self._tos.append(email.get())

    @property
    def ccs(self):
        return self._ccs

    @ccs.setter
    def ccs(self, value):
        self._ccs = value

    def add_cc(self, email):
        if self._ccs is None:
            self._ccs = []
        self._ccs.append(email.get())

    @property
    def bccs(self):
        return self._bccs

    @bccs.setter
    def bccs(self, value):
        self._bccs = value

    def add_bcc(self, email):
        if self._bccs is None:
            self._bccs = []
        self._bccs.append(email.get())

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        self._headers = value

    def add_header(self, header):
        if self._headers is None:
            self._headers = []
        self._headers.append(header.get())

    @property
    def substitutions(self):
        return self._substitutions

    @substitutions.setter
    def substitutions(self, value):
        self.substitutions = value

    def add_substitution(self, substitution):
        if self._substitutions is None:
            self._substitutions = []
        self._substitutions.append(substitution.get())

    @property
    def custom_args(self):
        return self._custom_args

    @custom_args.setter
    def custom_args(self, value):
        self._custom_args = value

    def add_custom_arg(self, custom_arg):
        if self._custom_args is None:
            self._custom_args = []
        self._custom_args.append(custom_arg.get())

    @property
    def send_at(self):
        return self._send_at

    @send_at.setter
    def send_at(self, value):
        self._send_at = value

    def get(self):
        personalization = {}
        if self.tos is not None:
            personalization["to"] = self.tos

        if self.ccs is not None:
            personalization["cc"] = self.ccs

        if self.bccs is not None:
            personalization["bcc"] = self.bccs

        if self.subject is not None:
            personalization["subject"] = self.subject

        if self.headers is not None:
            headers = {}
            for key in self.headers:
                headers.update(key)
            personalization["headers"] = headers

        if self.substitutions is not None:
            substitutions = {}
            for key in self.substitutions:
                substitutions.update(key)
            personalization["substitutions"] = substitutions

        if self.custom_args is not None:
            custom_args = {}
            for key in self.custom_args:
                custom_args.update(key)
            personalization["custom_args"] = custom_args

        if self.send_at is not None:
            personalization["send_at"] = self.send_at
        return personalization


class Attachment(object):

    def __init__(self):
        self._content = None
        self._type = None
        self._filename = None
        self._disposition = None
        self._content_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    @property
    def disposition(self):
        return self._disposition

    @disposition.setter
    def disposition(self, value):
        self._disposition = value

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value

    def get(self):
        attachment = {}
        if self.content is not None:
            attachment["content"] = self.content

        if self.type is not None:
            attachment["type"] = self.type

        if self.filename is not None:
            attachment["filename"] = self.filename

        if self.disposition is not None:
            attachment["disposition"] = self.disposition

        if self.content_id is not None:
            attachment["content_id"] = self.content_id
        return attachment


class Category(object):

    def __init__(self, name=None):
        self._name = None
        if name is not None:
            self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def get(self):
        return self.name


class ASM(object):

    def __init__(self, group_id=None, groups_to_display=None):
        self._group_id = None
        self._groups_to_display = None

        if group_id is not None:
            self._group_id = group_id

        if groups_to_display is not None:
            self._groups_to_display = groups_to_display

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value

    @property
    def groups_to_display(self):
        return self._groups_to_display

    @groups_to_display.setter
    def groups_to_display(self, value):
        self._groups_to_display = value

    def get(self):
        asm = {}
        if self.group_id is not None:
            asm["group_id"] = self.group_id

        if self.groups_to_display is not None:
            asm["groups_to_display"] = self.groups_to_display
        return asm


class BCCSettings(object):

    def __init__(self, enable=None, email=None):
        self._enable = None
        self._email = None

        if enable is not None:
            self.enable = enable

        if email is not None:
            self.email = email

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    def get(self):
        bcc_settings = {}
        if self.enable is not None:
            bcc_settings["enable"] = self.enable

        if self.email is not None:
            email = self.email.get()
            bcc_settings["email"] = email["email"]
        return bcc_settings


class BypassListManagement(object):

    def __init__(self, enable=None):
        self._enable = None

        if enable is not None:
            self.enable = enable

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    def get(self):
        bypass_list_management = {}
        if self.enable is not None:
            bypass_list_management["enable"] = self.enable
        return bypass_list_management


class FooterSettings(object):

    def __init__(self, enable=None, text=None, html=None):
        self._enable = None
        self._text = None
        self._html = None

        if enable is not None:
            self.enable = enable

        if text is not None:
            self.text = text

        if html is not None:
            self.html = html

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, value):
        self._html = value

    def get(self):
        footer_settings = {}
        if self.enable is not None:
            footer_settings["enable"] = self.enable

        if self.text is not None:
            footer_settings["text"] = self.text

        if self.html is not None:
            footer_settings["html"] = self.html
        return footer_settings


class SandBoxMode(object):

    def __init__(self, enable=None):
        self._enable = None

        if enable is not None:
            self.enable = enable

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    def get(self):
        sandbox_mode = {}
        if self.enable is not None:
            sandbox_mode["enable"] = self.enable
        return sandbox_mode


class SpamCheck(object):

    def __init__(self, enable=None, threshold=None, post_to_url=None):
        self._enable = None
        self._threshold = None
        self._post_to_url = None

        if enable is not None:
            self.enable = enable

        if threshold is not None:
            self.threshold = threshold

        if post_to_url is not None:
            self.post_to_url = post_to_url

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        self._threshold = value

    @property
    def post_to_url(self):
        return self._post_to_url

    @post_to_url.setter
    def post_to_url(self, value):
        self._post_to_url = value

    def get(self):
        spam_check = {}
        if self.enable is not None:
            spam_check["enable"] = self.enable

        if self.threshold is not None:
            spam_check["threshold"] = self.threshold

        if self.post_to_url is not None:
            spam_check["post_to_url"] = self.post_to_url
        return spam_check


class MailSettings(object):

    def __init__(self):
        self._bcc_settings = None
        self._bypass_list_management = None
        self._footer_settings = None
        self._sandbox_mode = None
        self._spam_check = None

    @property
    def bcc_settings(self):
        return self._bcc_settings

    @bcc_settings.setter
    def bcc_settings(self, value):
        self._bcc_settings = value

    @property
    def bypass_list_management(self):
        return self._bypass_list_management

    @bypass_list_management.setter
    def bypass_list_management(self, value):
        self._bypass_list_management = value

    @property
    def footer_settings(self):
        return self._footer_settings

    @footer_settings.setter
    def footer_settings(self, value):
        self._footer_settings = value

    @property
    def sandbox_mode(self):
        return self._sandbox_mode

    @sandbox_mode.setter
    def sandbox_mode(self, value):
        self._sandbox_mode = value

    @property
    def spam_check(self):
        return self._spam_check

    @spam_check.setter
    def spam_check(self, value):
        self._spam_check = value

    def get(self):
        mail_settings = {}
        if self.bcc_settings is not None:
            mail_settings["bcc"] = self.bcc_settings.get()

        if self.bypass_list_management is not None:
            mail_settings[
                "bypass_list_management"] = self.bypass_list_management.get()

        if self.footer_settings is not None:
            mail_settings["footer"] = self.footer_settings.get()

        if self.sandbox_mode is not None:
            mail_settings["sandbox_mode"] = self.sandbox_mode.get()

        if self.spam_check is not None:
            mail_settings["spam_check"] = self.spam_check.get()
        return mail_settings


class ClickTracking(object):

    def __init__(self, enable=None, enable_text=None):
        self._enable = None
        self._enable_text = None

        if enable is not None:
            self.enable = enable

        if enable_text is not None:
            self.enable_text = enable_text

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    @property
    def enable_text(self):
        return self._enable_text

    @enable_text.setter
    def enable_text(self, value):
        self._enable_text = value

    def get(self):
        click_tracking = {}
        if self.enable is not None:
            click_tracking["enable"] = self.enable

        if self.enable_text is not None:
            click_tracking["enable_text"] = self.enable_text
        return click_tracking


class OpenTracking(object):

    def __init__(self, enable=None, substitution_tag=None):
        self._enable = None
        self._substitution_tag = None

        if enable is not None:
            self.enable = enable
        if substitution_tag is not None:
            self.substitution_tag = substitution_tag

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    @property
    def substitution_tag(self):
        return self._substitution_tag

    @substitution_tag.setter
    def substitution_tag(self, value):
        self._substitution_tag = value

    def get(self):
        open_tracking = {}
        if self.enable is not None:
            open_tracking["enable"] = self.enable

        if self.substitution_tag is not None:
            open_tracking["substitution_tag"] = self.substitution_tag
        return open_tracking


class SubscriptionTracking(object):

    def __init__(self, enable=None, text=None, html=None, substitution_tag=None):
        self._enable = None
        self._text = None
        self._html = None
        self._substitution_tag = None

        if enable is not None:
            self.enable = enable
        if text is not None:
            self.text = text
        if html is not None:
            self.html = html
        if substitution_tag is not None:
            self.substitution_tag = substitution_tag

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, value):
        self._html = value

    @property
    def substitution_tag(self):
        return self._substitution_tag

    @substitution_tag.setter
    def substitution_tag(self, value):
        self._substitution_tag = value

    def get(self):
        subscription_tracking = {}
        if self.enable is not None:
            subscription_tracking["enable"] = self.enable

        if self.text is not None:
            subscription_tracking["text"] = self.text

        if self.html is not None:
            subscription_tracking["html"] = self.html

        if self.substitution_tag is not None:
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
        self._enable = None
        self._utm_source = None
        self._utm_medium = None
        self._utm_term = None
        self._utm_content = None
        self._utm_campaign = None

        if enable is not None:
            self.enable = enable
        if utm_source is not None:
            self.utm_source = utm_source
        if utm_medium is not None:
            self.utm_medium = utm_medium
        if utm_term is not None:
            self.utm_term = utm_term
        if utm_content is not None:
            self.utm_content = utm_content
        if utm_campaign is not None:
            self.utm_campaign = utm_campaign

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    @property
    def utm_source(self):
        return self._utm_source

    @utm_source.setter
    def utm_source(self, value):
        self._utm_source = value

    @property
    def utm_medium(self):
        return self._utm_medium

    @utm_medium.setter
    def utm_medium(self, value):
        self._utm_medium = value

    @property
    def utm_term(self):
        return self._utm_term

    @utm_term.setter
    def utm_term(self, value):
        self._utm_term = value

    @property
    def utm_content(self):
        return self._utm_content

    @utm_content.setter
    def utm_content(self, value):
        self._utm_content = value

    @property
    def utm_campaign(self):
        return self._utm_campaign

    @utm_campaign.setter
    def utm_campaign(self, value):
        self._utm_campaign = value

    def get(self):
        ganalytics = {}
        if self.enable is not None:
            ganalytics["enable"] = self.enable
        if self.utm_source is not None:
            ganalytics["utm_source"] = self.utm_source
        if self.utm_medium is not None:
            ganalytics["utm_medium"] = self.utm_medium
        if self.utm_term is not None:
            ganalytics["utm_term"] = self.utm_term
        if self.utm_content is not None:
            ganalytics["utm_content"] = self.utm_content
        if self.utm_campaign is not None:
            ganalytics["utm_campaign"] = self.utm_campaign
        return ganalytics


class TrackingSettings(object):

    def __init__(self):
        self._click_tracking = None
        self._open_tracking = None
        self._subscription_tracking = None
        self._ganalytics = None

    @property
    def click_tracking(self):
        return self._click_tracking

    @click_tracking.setter
    def click_tracking(self, value):
        self._click_tracking = value

    @property
    def open_tracking(self):
        return self._open_tracking

    @open_tracking.setter
    def open_tracking(self, value):
        self._open_tracking = value

    @property
    def subscription_tracking(self):
        return self._subscription_tracking

    @subscription_tracking.setter
    def subscription_tracking(self, value):
        self._subscription_tracking = value

    @property
    def ganalytics(self):
        return self._ganalytics

    @ganalytics.setter
    def ganalytics(self, value):
        self._ganalytics = value

    def get(self):
        tracking_settings = {}
        if self.click_tracking is not None:
            tracking_settings["click_tracking"] = self.click_tracking.get()
        if self.open_tracking is not None:
            tracking_settings["open_tracking"] = self.open_tracking.get()
        if self.subscription_tracking is not None:
            tracking_settings[
                "subscription_tracking"] = self.subscription_tracking.get()
        if self.ganalytics is not None:
            tracking_settings["ganalytics"] = self.ganalytics.get()
        return tracking_settings
