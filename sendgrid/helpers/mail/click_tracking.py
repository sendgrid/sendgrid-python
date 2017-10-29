class ClickTracking(object):

    def __init__(self, enable=None, enable_text=None):
        self.enable = enable
        self.enable_text = enable_text

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    @property
    def enable_text(self):
        return self._enable_text

    @enable_text.setter
    def enable_text(self, value):
        self._enable_text = value

    def get(self):
        click_tracking = {}
        if self.enable is not None:
            click_tracking["enable"] = self.enable

        if self.enable_text is not None:
            click_tracking["enable_text"] = self.enable_text
        return click_tracking
