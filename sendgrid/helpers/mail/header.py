class Header(object):

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def get(self):
        header = {}
        if self.key is not None and self.value is not None:
            header[self.key] = self.value
        return header
