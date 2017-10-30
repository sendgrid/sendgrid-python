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
