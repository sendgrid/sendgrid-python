class BCCSettings(object):

    def __init__(self, enable=None, email=None):
        self.enable = enable
        self.email = email

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    def get(self):
        bcc_settings = {}
        if self.enable is not None:
            bcc_settings["enable"] = self.enable

        if self.email is not None:
            email = self.email.get()
            bcc_settings["email"] = email["email"]
        return bcc_settings
