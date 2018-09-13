try:
    import rfc822
except ImportError:
    import email.utils as rfc822

import sys
if sys.version_info[:3] >= (3, 5, 0):
    import html
    html_entity_decode = html.unescape
else:
    try:
        # Python 2.6-2.7
        from HTMLParser import HTMLParser
    except ImportError:
        # Python < 3.5
        from html.parser import HTMLParser
    __html_parser__ = HTMLParser()
    html_entity_decode = __html_parser__.unescape


class Email(object):
    """An email address with an optional name."""

    def __init__(self, email=None, name=None):
        """Create an Email with the given address and name.

        Either fill the separate name and email fields, or pass all information
        in the email parameter (e.g. email="dude Fella <example@example.com>").
        :param email: Email address, or name and address in standard format.
        :type email: string
        :param name: Name for this sender or recipient.
        :type name: string
        """
        if email and not name:
            # allows passing emails as "dude Fella <example@example.com>"
            self.parse_email(email)
        else:
            # allows backwards compatibility for Email(email, name)
            self.email = email
            self.name = name

    @property
    def name(self):
        """Name associated with this email.

        :rtype: string
        """
        return self._name

    @name.setter
    def name(self, value):
        if not (value is None or isinstance(value, str)):
            raise TypeError('name must be of type string.')

        if value is not None and (',' in value or ';' in value):
            value = html_entity_decode(value)
            value = '"' + value + '"'
        self._name = value

    @property
    def email(self):
        """Email address.

        See http://tools.ietf.org/html/rfc3696#section-3 and its errata
        http://www.rfc-editor.org/errata_search.php?rfc=3696 for information
        on valid email addresses.
        """
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    def get(self):
        """
        Get a JSON-ready representation of this Email.

        :returns: This Email, ready for use in a request body.
        :rtype: dict
        """
        email = {}
        if self.name is not None:
            email["name"] = self.name

        if self.email is not None:
            email["email"] = self.email
        return email

    def parse_email(self, email_info):
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
