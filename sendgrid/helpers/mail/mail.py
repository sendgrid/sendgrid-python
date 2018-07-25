"""v3/mail/send response body builder"""
from .personalization import Personalization
from .header import Header

class Mail(object):
    """Creates the response body for v3/mail/send"""
    def __init__(
            self, from_email=None, subject=None, to_email=None, content=None):
        self._personalizations = None
        self._contents = None
        self._attachments = None
        self._sections = None
        self._headers = None
        self._categories = None
        self._custom_args = None
        self.from_email = None
        self.subject = None
        self.template_id = None
        self.send_at = None
        self.batch_id = None
        self.asm = None
        self.ip_pool_name = None
        self.mail_settings = None
        self.tracking_settings = None
        self.reply_to = None

        # Minimum required to send a single email
        if to_email:
            personalization = Personalization()
            personalization.add_to(to_email)
            self.add_personalization(personalization)
        if subject:
            self.subject = subject
        if from_email:
            self.from_email = from_email
        if content:
            self.add_content(content)

    def __str__(self):
        return str(self.get())

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
            'sections': self._flatten_dictionaries(self.sections),
            'headers': self._flatten_dictionaries(self.headers),
            'categories': [c.get() for c in self.categories or []],
            'custom_args': self._flatten_dictionaries(self.custom_args),
            'send_at': self.send_at,
            'batch_id': self.batch_id,
            'asm': self._get_or_none(self.asm),
            'ip_pool_name': self.ip_pool_name,
            'mail_settings': self._get_or_none(self.mail_settings),
            'tracking_settings': self._get_or_none(self.tracking_settings),
            'reply_to': self._get_or_none(self.reply_to),
        }

        return dict((key, value) for key, value in mail.items()
                    if value is not None and value != [] and value != {})

    def _get_or_none(self, from_obj):
        return from_obj.get() if from_obj is not None else None

    def _flatten_dictionaries(self, dicts):
        list_of_dicts = [d.get() for d in dicts or []]
        return dict((k, v) for d in list_of_dicts for k, v in d.items())

    @property
    def personalizations(self):
        return self._personalizations

    def add_personalization(self, personalizations):
        self._personalizations = self._ensure_append(
            personalizations, self._personalizations)

    @property
    def contents(self):
        return self._contents

    def add_content(self, content):
        # Text content should be before HTML content
        if content._type == "text/plain":
            self._contents = self._ensure_insert(content, self._contents)
        else:
            self._contents = self._ensure_append(content, self._contents)

    @property
    def attachments(self):
        return self._attachments

    def add_attachment(self, attachment):
        self._attachments = self._ensure_append(attachment, self._attachments)

    @property
    def sections(self):
        return self._sections

    def add_section(self, section):
        self._sections = self._ensure_append(section, self._sections)

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
    def categories(self):
        return self._categories

    def add_category(self, category):
        self._categories = self._ensure_append(category, self._categories)

    @property
    def custom_args(self):
        return self._custom_args

    def add_custom_arg(self, custom_arg):
        self._custom_args = self._ensure_append(custom_arg, self._custom_args)

    def _ensure_append(self, new_items, append_to):
        append_to = append_to or []
        append_to.append(new_items)
        return append_to

    def _ensure_insert(self, new_items, insert_to):
        insert_to = insert_to or []
        insert_to.insert(0, new_items)
        return insert_to