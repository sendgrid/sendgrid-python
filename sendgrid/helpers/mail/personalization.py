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

    @property
    def custom_args(self):
        return self._custom_args

    @custom_args.setter
    def custom_args(self, value):
        self._custom_args = value

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
