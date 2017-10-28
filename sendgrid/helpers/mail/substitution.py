class Substitution(object):

    def __init__(self, key=None, value=None):
        self._key = None
        self._value = None

        if key is not None:
            self.key = key

        if value is not None:
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
        substitution = {}
        if self.key is not None and self.value is not None:
            substitution[self.key] = self.value
        return substitution
