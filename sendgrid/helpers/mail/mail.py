"""v3/mail/send response body builder"""
from .personalization import Personalization
from .header import Header

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
        return str(self.get())

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