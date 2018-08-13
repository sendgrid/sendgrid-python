"""v3/mail/send response body builder"""
import io
import sys
import base64
import mimetypes
from .personalization import Personalization
from .header import Header


class Mail(object):
    """A request to be sent with the SendGrid v3 Mail Send API (v3/mail/send).

    Use get() to get the request body.
    """
    def __init__(self, 
                 from_email=None, 
                 subject=None, 
                 to_email=None, 
                 content=None):
        """Create a Mail object.

        If any parameters are not supplied, they must be set after initialization.
        :param from_email: Email address to send from.
        :type from_email: Email, optional
        :param subject: Subject line of emails.
        :type subject: string, optional
        :param to_email: Email address to send to.
        :type to_email: Email, optional
        :param content: Content of the message.
        :type content: Content, optional
        """
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
        self._personalizations = []
        self._contents = []
        self._attachments = []
        self._sections = []
        self._headers = []
        self._categories = []
        self._custom_args = []

        if from_email:
            self.from_email = from_email

        if subject:
            self.subject = subject

        if to_email:
            personalization = Personalization()
            personalization.add_to(to_email)
            self.add_personalization(personalization)

        if content:
            self.add_content(content)

    def __str__(self):
        """Get a JSON representation of this Mail request.

        :rtype: string
        """
        return str(self.get())

    def get(self):
        """Get a response body for this Mail.

        :rtype: dict
        """
        mail = {}

        if self.from_email is not None:
            mail["from"] = self.from_email.get()
  
        if self.subject is not None:
            mail["subject"] = self.subject

        if self.personalizations:
            mail["personalizations"] = [
                personalization.get()
                for personalization in self.personalizations
            ]

        if self.contents:
            mail["content"] = [ob.get() for ob in self.contents]

        if self.attachments:
            mail["attachments"] = [ob.get() for ob in self.attachments]

        if self.template_id is not None:
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
            mail["categories"] = [category.get() for category in
                                  self.categories]

        if self.custom_args:
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
        """The email from which this Mail will be sent.

        :rtype: string
        """
        return self._from_email

    @from_email.setter
    def from_email(self, value):
        self._from_email = value

    @property
    def subject(self):
        """The global, or "message level", subject of this Mail.

        This may be overridden by personalizations[x].subject.
        :rtype: string
        """
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value

    @property
    def template_id(self):
        """The id of a template that you would like to use.

        If you use a template that contains a subject and content (either text
        or html), you do not need to specify those at the personalizations nor
        message level.

        :rtype: int
        """

        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value

    @property
    def send_at(self):
        """A unix timestamp allowing you to specify when you want your email to
        be delivered. This may be overridden by the personalizations[x].send_at
        parameter. Scheduling more than 72 hours in advance is forbidden.

        :rtype: int
        """
        return self._send_at

    @send_at.setter
    def send_at(self, value):
        self._send_at = value

    @property
    def batch_id(self):
        """An ID for this batch of emails.

        This represents a batch of emails sent at the same time. Including a
        batch_id in your request allows you include this email in that batch,
        and also enables you to cancel or pause the delivery of that batch.
        For more information, see https://sendgrid.com/docs/API_Reference/Web_API_v3/cancel_schedule_send.html

        :rtype: int
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value

    @property
    def asm(self):
        """The ASM for this Mail.

        :rtype: ASM
        """
        return self._asm

    @asm.setter
    def asm(self, value):
        self._asm = value

    @property
    def mail_settings(self):
        """The MailSettings for this Mail.

        :rtype: MailSettings
        """
        return self._mail_settings

    @mail_settings.setter
    def mail_settings(self, value):
        self._mail_settings = value

    @property
    def tracking_settings(self):
        """The TrackingSettings for this Mail.

        :rtype: TrackingSettings
        """
        return self._tracking_settings

    @tracking_settings.setter
    def tracking_settings(self, value):
        self._tracking_settings = value

    @property
    def ip_pool_name(self):
        """The IP Pool that you would like to send this Mail email from.

        :rtype: string
        """
        return self._ip_pool_name

    @ip_pool_name.setter
    def ip_pool_name(self, value):
        self._ip_pool_name = value

    @property
    def reply_to(self):
        """The email address to use in the Reply-To header.

        :rtype: Email
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, value):
        self._reply_to = value

    @property
    def personalizations(self):
        """The Personalizations applied to this Mail.

        Each object within personalizations can be thought of as an envelope -
        it defines who should receive an individual message and how that
        message should be handled. A maximum of 1000 personalizations can be
        included.

        :rtype: list
        """
        return self._personalizations

    def add_personalization(self, personalizations):
        """Add a new Personalization to this Mail.

        :type personalizations: Personalization
        """
        self._personalizations.append(personalizations)

    @property
    def contents(self):
        """The Contents of this Mail. Must include at least one MIME type.

        :rtype: list(Content)
        """
        return self._contents

    def add_content(self, content):
        """Add a new Content to this Mail.  Usually the plaintext or HTML
        message contents.

        :type content: Content
        """
        if self._contents is None:
            self._contents = []
        
        # Text content should be before HTML content
        if content._type == "text/plain":
            self._contents.insert(0, content)
        else:
            self._contents.append(content)

    @property
    def attachments(self):
        """The attachments included with this Mail.

        :returns: List of Attachment objects.
        :rtype: list(Attachment)
        """
        return self._attachments

    def add_attachment(self, attachment):
        """Add an Attachment to this Mail.

        :type attachment: Attachment
        """
        self._attachments.append(attachment)

    @property
    def sections(self):
        """The sections included with this Mail.

        :returns: List of Section objects.
        :rtype: list(Section)
        """
        return self._sections

    def add_section(self, section):
        """Add a Section to this Mail.

        :type section: Section
        """
        self._sections.append(section)

    @property
    def headers(self):
        """The Headers included with this Mail.

        :returns: List of Header objects.
        :rtype: list(Header)
        """
        return self._headers

    def add_header(self, header):
        """Add a Header to this Mail.

        The header provided can be a Header or a dictionary with a single
        key-value pair.
        :type header: object
        """
        if isinstance(header, dict):
            (k, v) = list(header.items())[0]
            self._headers.append(Header(k, v))
        else:
            self._headers.append(header)

    @property
    def categories(self):
        """The Categories applied to this Mail.  Must not exceed 10 items

        :rtype: list(Category)
        """
        return self._categories

    def add_category(self, category):
        """Add a Category to this Mail.  Must be less than 255 characters.

        :type category: string
        """
        self._categories.append(category)

    @property
    def custom_args(self):
        """The CustomArgs attached to this Mail.

        Must not exceed 10,000 characters.
        :rtype: list(CustomArg)
        """
        return self._custom_args

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

    def _reopen_binary(self, f):
        mode = f.mode
        if 'b' not in mode:
            mode += 'b'
        return open(f.name, mode)

    @property
    def file(self):
        return None

    @file.setter
    def file(self, value):
        is_string = isinstance(value, str)
        is_file2 = (sys.version_info < (3, 0) and type(value) is file)
        is_file3 = (sys.version_info >= (3, 0) and isinstance(value, io.IOBase))
        is_file = is_file2 or is_file3

        if is_string:
            f = open(value, 'rb')
        elif is_file:
            f = self._reopen_binary(value)
        else:
            raise Exception("Invalid value type. Must be string with filename or file-like object")

        data = f.read()
        self.content = base64.b64encode(data).decode()
        self.filename = f.name
        mimetype, _ = mimetypes.guess_type(self.filename)
        if mimetype:
            print('type is {}'.format(mimetype))
            self.type = mimetype
        f.close()

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
