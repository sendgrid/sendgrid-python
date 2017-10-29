class OpenTracking(object):

    def __init__(self, enable=None, substitution_tag=None):
        self.enable = enable
        self.substitution_tag = substitution_tag

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    @property
    def substitution_tag(self):
        return self._substitution_tag

    @substitution_tag.setter
    def substitution_tag(self, value):
        self._substitution_tag = value

    def get(self):
        open_tracking = {}
        if self.enable is not None:
            open_tracking["enable"] = self.enable

        if self.substitution_tag is not None:
            open_tracking["substitution_tag"] = self.substitution_tag
        return open_tracking
