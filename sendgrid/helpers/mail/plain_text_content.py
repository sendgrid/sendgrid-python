from .content import Content
from .validators import ValidateAPIKey

class PlainTextContent(Content):
    """Plain text content to be included in your email.
    """

    def __init__(self, value):
        """Create a PlainTextContent with the specified MIME type and value.

        :param value: The actual text content.
        :type value: string, optional
        """
        self._validator = ValidateAPIKey()
        self.type = "text/plain"
        self.value = value

    @property
    def value(self):
        """The actual text content.

        :rtype: string
        """
        return self._value

    @value.setter
    def value(self, value):
        self._validator.validate_message_dict(value)
        self._value = value

    def get(self):
        """
        Get a JSON-ready representation of this PlainTextContent.

        :returns: This PlainTextContent, ready for use in a request body.
        :rtype: dict
        """
        content = {}
        content["type"] = "text/plain"
        content["value"] = self._value
        return content
