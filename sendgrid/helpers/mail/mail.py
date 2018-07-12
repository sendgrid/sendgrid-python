"""v3/mail/send response body builder"""
from .personalization import Personalization
from .header import Header

class Mail(object):
    """A request to be sent with the SendGrid v3 Mail Send API (v3/mail/send).

    Use get() to get the request body.
    """
    def __init__(self, 
                 from_email=None, 
                 to_emails=None,
                 subject=None, 
                 plain_text_content=None,
                 html_content=None):
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
            self.subject = subject.get()

        if to_emails:
            personalization = Personalization()
            personalization.add_to(to_emails)
            self.add_personalization(personalization)

        if plain_text_content:
            self.add_content(plain_text_content)
        
        if html_content:
            self.add_content(html_content)

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

        REQUEST_BODY_KEYS = [
            'attachments',
            'batch_id',
            'categories',
            'custom_args',
            'headers',
            'ip_pool_name',
            'personalizations',
            'sections',
            'send_at',
            'subject',
            'template_id'
        ]

        for key in REQUEST_BODY_KEYS:
            value = getattr(self, key, None)
            if value:
                mail[key] = value

        if self.contents:
            mail["content"] = self.contents

        if self.from_email:
            mail["from"] = self.from_email.get()


        if self.asm:
            mail["asm"] = self.asm.get()

        if self.mail_settings:
            mail["mail_settings"] = self.mail_settings.get()

        if self.tracking_settings:
            mail["tracking_settings"] = self.tracking_settings.get()

        if self.reply_to:
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

        :returns: List of dictionaries. Each dictionary is obtained by
        Personalization.get
        :rtype: list(dictionaries)
        """
        if self._personalizations is not None:
            return [
                personalization.get()
                for personalization in self._personalizations
            ]

    def add_personalization(self, personalizations):
        """Add a new Personalization to this Mail.

        :type personalizations: Personalization
        """
        self._personalizations.append(personalizations)

    @property
    def contents(self):
        """The Contents of this Mail. Must include at least one MIME type.
        
        :returns: List of dictionaries returned by content.get
        :rtype: list(Content)
        """
        if self._contents is not None:
            return[
                ob.get()
                for ob in self._contents
            ]
        return None

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

        :returns: List of dictionaries. Each dictionary is obtained by
        Attachment.get
        :rtype: list(dictionaries)
        """
        if self._attachments:
            return [
                ob.get()
                for ob in self._attachments
            ]
        return None

    def add_attachment(self, attachment):
        """Add an Attachment to this Mail.

        :type attachment: Attachment
        """
        self._attachments.append(attachment)

    @property
    def sections(self):
        """The sections included with this Mail.

        :returns: List of of dictionaries. Each dictionary is obtained by
        Section.get
        :rtype: list(dictionaries)
        """
        if self._sections:
            return self.update_objects(self._sections)
        return None

    def add_section(self, section):
        """Add a Section to this Mail.

        :type section: Section
        """
        self._sections.append(section)

    @property
    def headers(self):
        """The Headers included with this Mail.

        :returns: List of dictionaries. Each dictionary is obtained by
        Header.get
        :rtype: list(dictionaries)
        """
        if self._headers:
            return self.update_objects(self._headers)
        return None

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

        :returns: List of dictionaries. Each dictionary is obtained by 
        Category.get
        :rtype: list(dictionaries)
        """
        if self._categories:
            return [
                category.get 
                for category in self._categories
            ]

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
        if self._custom_args:
            return self.update_objects(self._custom_args)
        return None

    def add_custom_arg(self, custom_arg):
        if self._custom_args is None:
            self._custom_args = []
        self._custom_args.append(custom_arg)
    
    def update_objects(self, property):
        objects = {}
        for key in property:
            objects.update(key.get())
        return objects

        

