class FooterSettings(object):

    def __init__(self, enable=None, text=None, html=None):
        self._enable = None
        self._text = None
        self._html = None

        if enable is not None:
            self.enable = enable

        if text is not None:
            self.text = text

        if html is not None:
            self.html = html

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, value):
        self._html = value

    def get(self):
        footer_settings = {}
        if self.enable is not None:
            footer_settings["enable"] = self.enable

        if self.text is not None:
            footer_settings["text"] = self.text

        if self.html is not None:
            footer_settings["html"] = self.html
        return footer_settings
