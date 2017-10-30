class Content(object):
    def __init__(self, type_=None, value=None):
        self._type = None
        self._value = None

        if type_ is not None:
            self.type = type_

        if value is not None:
            self.value = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def get(self):
        content = {}
        if self.type is not None:
            content["type"] = self.type

        if self.value is not None:
            content["value"] = self.value
        return content
