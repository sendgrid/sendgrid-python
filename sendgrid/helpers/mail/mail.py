"""v3/mail/send response body builder"""
from .personalization import Personalization
from .header import Header

################################################################
# Various types of extensible SendGrid related exceptions
################################################################

class SendGridException(Exception):
    """Wrapper/default SendGrid-related exception"""
    pass


class APIKeyIncludedException(SendGridException):
    """Exception raised for when SendGrid API Key included in message text

        Attributes:
            expression -- input expression in which the error occurred
            message -- explanation of the error
    """

    def __init__(self, 
                 expression="Email body", 
                 message="SendGrid API Key detected"):
        self.expression = expression
        self.message = message


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

        If parameters are supplied, all parameters must be present.
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
        self._personalizations = None
        self._contents = None
        self._attachments = None
        self._sections = None
        self._headers = None
        self._categories = None
        self._custom_args = None
        self._validator = ValidateAPIKey()

        # Minimum required to send an email
        if from_email and subject and to_email and content:
            self.from_email = from_email
            self.subject = subject
            personalization = Personalization()
            personalization.add_to(to_email)
            self.add_personalization(personalization)
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
        self._validator.validate_message_text(value)
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
        if self._personalizations is None:
            self._personalizations = []
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
        if self._attachments is None:
            self._attachments = []
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

        :type attachment: Section
        """
        if self._sections is None:
            self._sections = []
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
        if self._headers is None:
            self._headers = []
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
        if self._categories is None:
            self._categories = []
        self._categories.append(category)

    @property
    def custom_args(self):
        return self._custom_args

    def add_custom_arg(self, custom_arg):
      """Add a CustomArg to this Mail.
      
      :type custom_arg: CustomArg
      """
      
        if self._custom_args is None:
            self._custom_args = []
        self._custom_args.append(custom_arg)


################################################################
# Various types of Validators
################################################################

class ValidateAPIKey(object):
    """Validates content to ensure SendGrid API key is not present"""

    regexes = None

    def __init__(self, regex_strings=list(), use_default=True):
        """Constructor
        Args:
            regex_strings (list<str>): list of regex strings
            use_default (bool): Whether or not to include default regex
        """

        import re
        self.regexes = set()

        #Compile the regex strings into patterns, add them to our set
        for regex_string in regex_strings:
            self.regexes.add(re.compile(regex_string))

        if use_default:
            default_regex_string = 'SG\.[0-9a-zA-Z]+\.[0-9a-zA-Z]+'
            self.regexes.add(re.compile(default_regex_string))


    def validate_message_dict(self, request_body):
        """With the JSON dict that will be sent to SendGrid's API, 
            check the content for SendGrid API keys - throw exception if found

        Args:
            request_body (:obj:`dict`): message parameter that is
                                            an argument to: mail.send.post()

        Raises:
            APIKeyIncludedException: If any content in request_body matches regex
        """

        #Handle string in edge-case
        if isinstance(request_body, str):
            self.validate_message_text(request_body)

        #Default param
        elif isinstance(request_body, dict):
            if "content" in request_body:
                contents = request_body["content"]

                for content in contents:
                    if "value" in content and "type" in content:
                        if content["type"] == "text/html" or isinstance(content["value"], str):
                            message_text = content["value"]
                            self.validate_message_text(message_text)


    def validate_message_text(self, message_string):
        """With a message string, check to see if it contains a SendGrid API Key
            If a key is found, throw an exception

        Args:
            message_string (str): message that will be sent

        Raises:
            APIKeyIncludedException: If message_string matches a regex string
        """

        if isinstance(message_string, str):
            for regex in self.regexes:
                if regex_pattern.match(message_string) is not None:
                    raise APIKeyIncludedException()


################################################################
# The following objects are meant to be extended with validation
################################################################

class Email(object):

    def __init__(self, email=None, name=None):
        self._name = None
        self._email = None
        if name or email:
            if not name:
                # allows passing emails as "dude Fella <example@example.com>"
                self.parse_email(email)
            else:
                #allows backwards compatibility for Email(email, name)
                if email is not None:
                    self.email = email
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

    def parse_email(self, email_info):
        try:
            import rfc822
        except ImportError:
            import email.utils as rfc822
        
        name, email = rfc822.parseaddr(email_info)
        
        # more than likely a string was passed here instead of an email address
        if "@" not in email:
            name = email
            email = None

        if not name:
            name = None
            
        if not email:
            email = None

        self.name = name
        self.email = email
        return name, email

class Content(object):

    def __init__(self, type_=None, value=None):
        self._type = None
        self._value = None
        self._validator = ValidateAPIKey()

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
        self._validator.validate_message_dict(value)
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
        self._validator.validate_message_dict(value)

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
        self._validator.validate_message_dict(value)
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
        self._key = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

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
      """The CustomArgs attached to this Mail.
          Must not exceed 10,000 characters.
      :rtype: list(CustomArg)
      """
        
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

        
    def add_custom_arg(self, custom_arg):
        """Add a CustomArg to this Mail.

        :type custom_arg: CustomArg
        """
        if self._custom_args is None:
            self._custom_args = []
        self._custom_args.append(custom_arg)
    
    def get(self):
      """The CustomArgs attached to this Mail.
          Must not exceed 10,000 characters.
      :rtype: list(CustomArg)
      """
      custom_arg = {}
      if self.key is not None and self.value is not None:
          custom_arg[self.key] = self.value
      return custom_arg
