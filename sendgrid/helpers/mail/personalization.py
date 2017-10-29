class Personalization(object):

    def __init__(self):
        self._tos = []
        self._ccs = []
        self._bccs = []
        self._subject = None
        self._headers = []
        self._substitutions = []
        self._custom_args = []
        self._send_at = None

    @property
    def tos(self):
        return self._tos

    @tos.setter
    def tos(self, value):
        self._tos = value

    def add_to(self, email):
        self._tos.append(email.get())

    @property
    def ccs(self):
        return self._ccs

    @ccs.setter
    def ccs(self, value):
        self._ccs = value

    def add_cc(self, email):
        self._ccs.append(email.get())

    @property
    def bccs(self):
        return self._bccs

    @bccs.setter
    def bccs(self, value):
        self._bccs = value

    def add_bcc(self, email):
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
        self._headers.append(header.get())

    @property
    def substitutions(self):
        return self._substitutions

    @substitutions.setter
    def substitutions(self, value):
        self.substitutions = value

    def add_substitution(self, substitution):
        self._substitutions.append(substitution.get())

    @property
    def custom_args(self):
        return self._custom_args

    @custom_args.setter
    def custom_args(self, value):
        self._custom_args = value

    def add_custom_arg(self, custom_arg):
        self._custom_args.append(custom_arg.get())

    @property
    def send_at(self):
        return self._send_at

    @send_at.setter
    def send_at(self, value):
        self._send_at = value

    def get(self):
        personalization = {}
        if self.tos:
            personalization["to"] = self.tos

        if self.ccs:
            personalization["cc"] = self.ccs

        if self.bccs:
            personalization["bcc"] = self.bccs

        if self.subject is not None:
            personalization["subject"] = self.subject

        if self.headers:
            headers = {}
            for key in self.headers:
                headers.update(key)
            personalization["headers"] = headers

        if self.substitutions:
            substitutions = {}
            for key in self.substitutions:
                substitutions.update(key)
            personalization["substitutions"] = substitutions

        if self.custom_args:
            custom_args = {}
            for key in self.custom_args:
                custom_args.update(key)
            personalization["custom_args"] = custom_args

        if self.send_at is not None:
            personalization["send_at"] = self.send_at
        return personalization
