class SandBoxMode(object):

    def __init__(self, enable=None):
        self.enable = enable

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    def get(self):
        sandbox_mode = {}
        if self.enable is not None:
            sandbox_mode["enable"] = self.enable
        return sandbox_mode
