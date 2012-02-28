import rfc822
from header import SmtpApiHeader


class Message(object):
    """
    Sendgrid Message
    """

    def __init__(self, addr_from, subject, text="", html=""):
        """
        Constructs Sendgrid Message object

        Args:
            addr_from: From address, email "example@example.com" or tuple ("example@example.com", "John, Doe")
            subject: Email subject
            text: Email content, plain text
            html: Email content, html

        Returns:
            self

        Raises:
            ValueError: on invalid arguments
        """
        if not (text + html):
            raise ValueError("Either html or text should be provided")

        self.from_name = ''
        self.from_address = addr_from
        if isinstance(addr_from, tuple):
            (self.from_address, self.from_name) = addr_from
        self.to_name = []
        self.reply_to = ''
        self.to = []
        self.subject = subject
        self.html = html
        self.text = text
        self.cc = []
        self.bcc = []
        self.headers = {}
        self.attachments = []
        self.header = SmtpApiHeader()
        self.date = rfc822.formatdate()


    def add_to(self, recipients, names = None):
        """
        Add recipient

        Args:
            recipients: recipient, accepts string, list or dict
                if dict is passed, "To" field will be ignored and batch sending with substitution triggered
            names:  recipient names, string or list

        Returns:
            self
        """
        if not recipients:
            raise ValueError('No recipients')

        if isinstance(recipients, (str, unicode)):
            self.to += [recipients]
            if names:
                self.to_name += [names]
        elif isinstance(recipients, dict):
            subvals = {}
            to = []
            for email in recipients:
                to.append(email)
                for subval in recipients[email]:
                    if not subval in subvals:
                        subvals[subval] = []

                    subvals[subval].append(recipients[email][subval])

            for subval in subvals:
                if len(subvals[subval]) != len(to):
                    self.header = SmtpApiHeader()
                    raise ValueError('Sub values count should be equal to recipients count')
                self.header.add_sub_val(subval, subvals[subval])

            self.header.add_to(to)
            self.to = [to[0]]
        else:
            self.to += recipients
            if names:
                self.to_name += names

        return self


    def add_cc(self, recipients):
        """
        Add CC recipients

        Args:
            recipients: Email address or list of email addresses

        Returns:
            self
        """
        if isinstance(recipients, (str, unicode)):
            self.cc += [recipients]
        else:
            self.cc += recipients

        return self


    def add_bcc(self, recipients):
        """
        Add BCC recipients

        Args:
            recipients: Email address or list of email addresses

        Returns:
            self
        """
        if isinstance(recipients, (str, unicode)):
            self.bcc += [recipients]
        else:
            self.bcc += recipients

        return self


    def add_attachment(self, name, file, cid=None):
        """
        Add attachment to email

        Args:
            name: name of the file as seen in email
            file: path to file or data string
            cid: Content-ID header, optional

        Returns:
            self
        """
        self.attachments.append({'name': name, 'file': file, 'cid': cid})

        return self


    def add_category(self, category):
        """
        Add category to the list of message categories (http://docs.sendgrid.com/documentation/delivery-metrics/categories/)

        Args:
            category: Category name or list of category names

        Returns:
            self
        """
        if isinstance(category, (str, unicode)):
            self.header.add_category(category)
        else:
            for cat in category:
                self.header.add_category(cat)

        return self


    def set_unique_arguments(self, arguments):
        """
        Set message unique arguments (http://docs.sendgrid.com/documentation/api/smtp-api/developers-guide/unique-arguments/)

        Args:
            arguments: Message unique arguments, dict: {"customerAccountNumber": "55555", "activationAttempt": "1"}

        Returns:
            self
        """
        self.header.set_unique_args(arguments)

        return self


    def add_unique_argument(self, key, value):
        """
        Add unique argument to message

        Args:
            key: Key of unique argument
            value: Value of unique argument

        Returns:
            self
        """
        self.header.add_unique_arg(key, value)

        return self


    def set_sections(self, value):
        """
        Set sections (http://docs.sendgrid.com/documentation/api/smtp-api/developers-guide/section-tags/)

        Args:
            value: Sections, dict: {"section1": "Section1 Value", "section2": "Section2 Value"}

        Returns:
            self
        """
        self.header.set_section(value)

        return self


    def add_section(self, key, value):
        """
        Add section (http://docs.sendgrid.com/documentation/api/smtp-api/developers-guide/section-tags/)

        Args:
            value: Sections, dict: {"section1": "Section1 Value", "section2": "Section2 Value"}

        Returns:
            self
        """
        self.header.add_section(key, value)

        return self


    def add_header(self, key, value):
        """
        Add header to message

        Args:
            key: Message header i.e. "X-MAILER"
            value: Header value i.e. "Sendgrid"

        Returns:
            self
        """
        self.headers[key] = value

        return self


    def add_filter_setting(self, fltr, setting, value):
        """
        Add filter setting (http://docs.sendgrid.com/documentation/api/smtp-api/filter-settings/)

        Args:
            fltr: Filter name i.e. "gravatar"
            setting: Filter setting i.e. "enable"
            value: Setting value i.e. 1

        Returns:
            self
        """
        self.header.add_filter_setting(fltr, setting, value)

        return self