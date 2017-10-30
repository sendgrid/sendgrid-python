class Attachment(object):

    def __init__(self):
        self._content = None
        self._type = None
        self._filename = None
        self._disposition = None
        self._content_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    @property
    def disposition(self):
        return self._disposition

    @disposition.setter
    def disposition(self, value):
        self._disposition = value

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value

    def get(self):
        attachment = {}
        if self.content is not None:
            attachment["content"] = self.content

        if self.type is not None:
            attachment["type"] = self.type

        if self.filename is not None:
            attachment["filename"] = self.filename

        if self.disposition is not None:
            attachment["disposition"] = self.disposition

        if self.content_id is not None:
            attachment["content_id"] = self.content_id
        return attachment
