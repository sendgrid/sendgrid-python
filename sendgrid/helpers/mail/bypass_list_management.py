class BypassListManagement(object):

    def __init__(self, enable=None):
        self._enable = None

        if enable is not None:
            self.enable = enable

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    def get(self):
        bypass_list_management = {}
        if self.enable is not None:
            bypass_list_management["enable"] = self.enable
        return bypass_list_management
