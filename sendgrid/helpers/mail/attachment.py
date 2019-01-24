class Attachment(object):
    """An attachment to be included with an email."""

    def __init__(self, content=None, type_=None, filename=None, disposition=None, content_id=None):
        """Create an Attachment

        :param content: The Base64 encoded content of the attachment
        :type content: string, optional
        :param type: The MIME type of the content you are attaching
        :type type string, optional
        :param filename: The filename of the attachment
        :type filename: string, optional
        :param disposition: The content-disposition of the attachment, specifying display style.
                            Specifies how you would like the attachment to be displayed.
                            - "inline" results in the attached file being displayed automatically
                                within the message.
                            - "attachment" results in the attached file requiring some action to
                                display (e.g. opening or downloading the file).
                            If unspecified, "attachment" is used. Must be one of the two choices.
        :type disposition: string, optional
        :param content_id: The content id for the attachment.
                           This is used when the disposition is set to "inline" and the attachment
                           is an image, allowing the file to be displayed within the email body.
        :type content_id: string, optional
        """
        self._content = None
        self._type = None
        self._filename = None
        self._disposition = None
        self._content_id = None

        if content is not None:
            self.content = content
        
        if type_ is not None:
            self.type = type_
        
        if filename is not None:
            self.filename = filename
        
        if disposition is not None:
            self.disposition = disposition
        
        if content_id is not None:
            self.content_id = content_id

    @property
    def content(self):
        """The Base64 encoded content of the attachment.

        :rtype: string
        """
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def type(self):
        """The MIME type of the content you are attaching.

        :rtype: string
        """
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def filename(self):
        """The filename of the attachment.

        :rtype: string
        """
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    @property
    def disposition(self):
        """The content-disposition of the attachment, specifying display style.

        Specifies how you would like the attachment to be displayed.
         - "inline" results in the attached file being displayed automatically
            within the message.
         - "attachment" results in the attached file requiring some action to
            display (e.g. opening or downloading the file).
        If unspecified, "attachment" is used. Must be one of the two choices.

        :rtype: string
        """
        return self._disposition

    @disposition.setter
    def disposition(self, value):
        self._disposition = value

    @property
    def content_id(self):
        """The content id for the attachment.

        This is used when the disposition is set to "inline" and the attachment
        is an image, allowing the file to be displayed within the email body.

        :rtype: string
        """
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value

    def get(self):
        """
        Get a JSON-ready representation of this Attachment.

        :returns: This Attachment, ready for use in a request body.
        :rtype: dict
        """
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
