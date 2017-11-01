class Category(object):

    def __init__(self, name=None):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def get(self):
        return self.name
