class MailSettings(object):

    def __init__(self):
        self._bcc_settings = None
        self._bypass_list_management = None
        self._footer_settings = None
        self._sandbox_mode = None
        self._spam_check = None

    @property
    def bcc_settings(self):
        return self._bcc_settings

    @bcc_settings.setter
    def bcc_settings(self, value):
        self._bcc_settings = value

    @property
    def bypass_list_management(self):
        return self._bypass_list_management

    @bypass_list_management.setter
    def bypass_list_management(self, value):
        self._bypass_list_management = value

    @property
    def footer_settings(self):
        return self._footer_settings

    @footer_settings.setter
    def footer_settings(self, value):
        self._footer_settings = value

    @property
    def sandbox_mode(self):
        return self._sandbox_mode

    @sandbox_mode.setter
    def sandbox_mode(self, value):
        self._sandbox_mode = value

    @property
    def spam_check(self):
        return self._spam_check

    @spam_check.setter
    def spam_check(self, value):
        self._spam_check = value

    def get(self):
        mail_settings = {}
        if self.bcc_settings is not None:
            mail_settings["bcc"] = self.bcc_settings.get()

        if self.bypass_list_management is not None:
            mail_settings[
                "bypass_list_management"] = self.bypass_list_management.get()

        if self.footer_settings is not None:
            mail_settings["footer"] = self.footer_settings.get()

        if self.sandbox_mode is not None:
            mail_settings["sandbox_mode"] = self.sandbox_mode.get()

        if self.spam_check is not None:
            mail_settings["spam_check"] = self.spam_check.get()
        return mail_settings
