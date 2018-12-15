"""v3/mail/send response body builder"""
from .personalization import Personalization
from .header import Header
from .email import Email
from .content import Content
from .subject import Subject

class Mail(object):
    """Creates the response body for v3/mail/send"""
    def __init__(
            self,
            from_email=None,
            subject=None,
            to_emails=None,
            plain_text_content=None,
            html_content=None,
            global_substitutions=None,
            is_multiple=False
        ):
        """Create Mail object
        
        :param from_email: The email address of the sender
        :type from_email: From, optional
        :param subject: The subject of the email
        :type subject: Subject, optional
        :param to_emails: The email address of the recipient
        :type to_emails: string, optional
        :param plain_text_content: The plain text body of the email
        :type plain_text_content: string, optional
        :param html_content: The html body of the email
        :type html_content: string, optional
        """
        self._attachments = None
        self._categories = None
        self._contents = None
        self._custom_args = None
        self._headers = None
        self._personalizations = []
        self._sections = None
        self._asm = None
        self._batch_id = None
        self._from_email = None
        self._ip_pool_name = None
        self._mail_settings = None
        self._reply_to = None
        self._send_at = None
        self._subject = None
        self._template_id = None
        self._tracking_settings = None

        # Minimum required data to send a single email
        if from_email is not None:
            self.from_email = from_email
        if subject is not None:
            self.subject = subject
        if to_emails is not None:
            self._set_emails(to_emails, global_substitutions, is_multiple)
        if plain_text_content is not None:
            self.add_content(plain_text_content)
        if html_content is not None:
            self.add_content(html_content)

    def __str__(self):
        return str(self.get())

    def _ensure_append(self, new_items, append_to, index=0):
        append_to = append_to or []
        append_to.insert(index, new_items)
        return append_to

    def _ensure_insert(self, new_items, insert_to):
        insert_to = insert_to or []
        insert_to.insert(0, new_items)
        return insert_to

    def _flatten_dicts(self, dicts):
        list_of_dicts = [d.get() for d in dicts or []]
        return {k: v for d in list_of_dicts for k, v in d.items()}

    def _get_or_none(self, from_obj):
        return from_obj.get() if from_obj is not None else None

    def _set_emails(self, emails, global_substitutions=None, is_multiple=False, p=0):
        # Send Multiple Emails to Multiple Recipients
        if is_multiple == True:
            if isinstance(emails, list):
                for email in emails:
                    if p == 0 and self._personalizations[p] == None:
                        personalization = Personalization()
                        self.add_personalization(personalization, index=p)
                    else:
                        self._personalizations[p].add_email(email)
            else:
                personalization = Personalization()
                personalization.add_email(emails)
                self.add_personalization(personalization)
            if global_substitutions is not None:
                if isinstance(global_substitutions, list):
                    for substitution in global_substitutions:
                        for p in self.personalizations:
                            p.add_substitution(substitution)
                else:
                    for p in self.personalizations:
                        p.add_substitution(global_substitutions)
        else:  
            try:
                personalization = self._personalizations[p]
                has_internal_personalization = True
            except IndexError:
                personalization = Personalization()
                has_internal_personalization = False

            if isinstance(emails, list):
                for email in emails:
                    personalization.add_email(email)
            else:
                personalization.add_email(emails)
            if global_substitutions is not None:
                if isinstance(global_substitutions, list):
                    for substitution in global_substitutions:
                        personalization.add_substitution(substitution)
                else:
                    personalization.add_substitution(global_substitutions)
            
            if not has_internal_personalization:
                self.add_personalization(personalization)

    @property
    def to(self):
        pass
    
    @to.setter
    def to(self, to_emails, global_substitutions=None, is_multiple=False, p=0):
        self._set_emails(to_emails, None, is_multiple=is_multiple, p=p)

    @property
    def cc(self):
        pass
    
    @cc.setter
    def cc(self, bcc_emails, global_substitutions=None, is_multiple=False, p=0):
        self._set_emails(bcc_emails, None, is_multiple=is_multiple, p=p)

    @property
    def bcc(self):
        pass
    
    @bcc.setter
    def bcc(self, bcc_emails, global_substitutions=None, is_multiple=False, p=0):
        self._set_emails(bcc_emails, None, is_multiple=is_multiple, p=p)

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
        # Text content should be before HTML content
        if content.type == "text/plain":
            self._contents = self._ensure_insert(content, self._contents)
        else:
            self._contents = self._ensure_append(content, self._contents)

    @property
    def headers(self):
        return self._headers

    @property
    def header(self):
        pass

    @header.setter
    def header(self, header):
        self.add_header(header)

    def add_header(self, header):
        if isinstance(header, dict):
            (k, v) = list(header.items())[0]
            self._headers = self._ensure_append(Header(k, v), self._headers)
        else:
            self._headers = self._ensure_append(header, self._headers)

    @property
    def personalizations(self):
        return self._personalizations

    def add_personalization(self, personalizations, index=0):
        self._personalizations = self._ensure_append(
            personalizations, self._personalizations, index)

    @property
    def sections(self):
        return self._sections

    def add_section(self, section):
        self._sections = self._ensure_append(section, self._sections)

    @property
    def asm(self):
        return self._asm
    
    @asm.setter
    def asm(self, value):
        self._asm = value

    @property
    def batch_id(self):
        return self._batch_id
    
    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value

    @property
    def from_email(self):
        return self._from_email
    
    @from_email.setter
    def from_email(self, value):
        self._from_email = value

    @property
    def ip_pool_name(self):
        return self._ip_pool_name
    
    @ip_pool_name.setter
    def ip_pool_name(self, value):
        self._ip_pool_name = value

    @property
    def mail_settings(self):
        return self._mail_settings
    
    @mail_settings.setter
    def mail_settings(self, value):
        self._mail_settings = value

    @property
    def reply_to(self):
        return self._reply_to
    
    @reply_to.setter
    def reply_to(self, value):
        self._reply_to = value

    @property
    def send_at(self):
        return self._send_at
    
    @send_at.setter
    def send_at(self, value):
        self._send_at = value

    @property
    def subject(self):
        return self._subject
    
    @subject.setter
    def subject(self, value):
        if isinstance(value, Subject):
            self._subject = value
        else:
            self._subject = Subject(value)

    @property
    def template_id(self):
        return self._template_id
    
    @template_id.setter
    def template_id(self, value):
        self._template_id = value

    @property
    def tracking_settings(self):
        return self._tracking_settings
    
    @tracking_settings.setter
    def tracking_settings(self, value):
        self._tracking_settings = value

    def get(self):
        """
        :return: request body dict
        """
        mail = {
            'from': self._get_or_none(self.from_email),
            'subject': self._get_or_none(self.subject),
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

    @classmethod
    def from_EmailMessage(cls, message):
        """Create a Mail object from an instance of
        email.message.EmailMessage.
        :type message: email.message.EmailMessage
        :rtype: Mail
        """
        mail = cls(
            from_email=Email(message.get('From')),
            subject=message.get('Subject'),
            to_emails=Email(message.get('To')),
        )
        try:
            body = message.get_content()
        except AttributeError:
            # Python2
            body = message.get_payload()
        mail.add_content(Content(
            message.get_content_type(),
            body.strip()
        ))
        for k, v in message.items():
            mail.add_header(Header(k, v))
        return mail
