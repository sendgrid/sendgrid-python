"""v3/mail/send response body builder"""
from .personalization import Personalization
from .header import Header


class Mail(object):
<<<<<<< eb542a51c5660e89b85814e1a66bb7c7eec49384
    """Creates the response body for v3/mail/send"""
    def __init__(
            self, from_email=None, subject=None, to_email=None, content=None):
        self._attachments = None
        self._categories = None
        self._contents = None
        self._custom_args = None
        self._headers = None
        self._personalizations = None
        self._sections = None
        self.asm = None
        self.batch_id = None
        self.from_email = None
        self.ip_pool_name = None
        self.mail_settings = None
        self.reply_to = None
        self.send_at = None
        self.subject = None
        self.template_id = None
        self.tracking_settings = None

        # Minimum required to send a single email
=======
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

>>>>>>> Change type of category in Mail.add_category from string to Category
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
        return str(self.get())

<<<<<<< eb542a51c5660e89b85814e1a66bb7c7eec49384
    def _ensure_append(self, new_items, append_to):
        append_to = append_to or []
        append_to.append(new_items)
        return append_to
=======
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
>>>>>>> Change type of category in Mail.add_category from string to Category

    def _ensure_insert(self, new_items, insert_to):
        insert_to = insert_to or []
        insert_to.insert(0, new_items)
        return insert_to

    def _flatten_dicts(self, dicts):
        list_of_dicts = [d.get() for d in dicts or []]
        return {k: v for d in list_of_dicts for k, v in d.items()}

    def _get_or_none(self, from_obj):
        return from_obj.get() if from_obj is not None else None

    @property
    def attachments(self):
        return self._attachments

    def add_attachment(self, attachment):
        self._attachments = self._ensure_append(attachment, self._attachments)

    @property
    def categories(self):
        return self._categories

    def add_category(self, category):
        self._categories = self._ensure_append(category, self._categories)

    @property
    def custom_args(self):
        return self._custom_args

    def add_custom_arg(self, custom_arg):
        self._custom_args = self._ensure_append(custom_arg, self._custom_args)

    @property
    def contents(self):
        return self._contents

    def add_content(self, content):
<<<<<<< eb542a51c5660e89b85814e1a66bb7c7eec49384
=======
        """Add a new Content to this Mail.  Usually the plaintext or HTML
        message contents.

        :type content: Content
        """
        if self._contents is None:
            self._contents = []

>>>>>>> Change type of category in Mail.add_category from string to Category
        # Text content should be before HTML content
        if content._type == "text/plain":
            self._contents = self._ensure_insert(content, self._contents)
        else:
            self._contents = self._ensure_append(content, self._contents)

    @property
    def headers(self):
        return self._headers

    def add_header(self, header):
        if isinstance(header, dict):
            (k, v) = list(header.items())[0]
            self._headers = self._ensure_append(Header(k, v), self._headers)
        else:
            self._headers = self._ensure_append(header, self._headers)

    @property
<<<<<<< eb542a51c5660e89b85814e1a66bb7c7eec49384
    def personalizations(self):
        return self._personalizations

    def add_personalization(self, personalizations):
        self._personalizations = self._ensure_append(
            personalizations, self._personalizations)
=======
    def categories(self):
        """The Categories applied to this Mail.  Must not exceed 10 items

        :rtype: list(Category)
        """
        return self._categories

    def add_category(self, category):
        """Add a Category to this Mail.

        :type category: Category
        """
        self._categories.append(category)
>>>>>>> Change type of category in Mail.add_category from string to Category

    @property
    def sections(self):
        return self._sections

    def add_section(self, section):
        self._sections = self._ensure_append(section, self._sections)

    def get(self):
        """
        :return: request body dict
        """
        mail = {
            'from': self._get_or_none(self.from_email),
            'subject': self.subject,
            'personalizations': [p.get() for p in self.personalizations or []],
            'content': [c.get() for c in self.contents or []],
            'attachments': [a.get() for a in self.attachments or []],
            'template_id': self.template_id,
            'sections': self._flatten_dicts(self.sections),
            'headers': self._flatten_dicts(self.headers),
            'categories': [c.get() for c in self.categories or []],
            'custom_args': self._flatten_dicts(self.custom_args),
            'send_at': self.send_at,
            'batch_id': self.batch_id,
            'asm': self._get_or_none(self.asm),
            'ip_pool_name': self.ip_pool_name,
            'mail_settings': self._get_or_none(self.mail_settings),
            'tracking_settings': self._get_or_none(self.tracking_settings),
            'reply_to': self._get_or_none(self.reply_to),
        }

        return {key: value for key, value in mail.items()
                if value is not None and value != [] and value != {}}
