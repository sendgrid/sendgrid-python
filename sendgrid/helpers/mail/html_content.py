from .content import Content
from .validators import ValidateAPIKey


class HtmlContent(Content):
    """HTML content to be included in your email."""

    def __init__(self, value = None):
        """Create an HtmlContent with the specified MIME type and value.

        :param value: The HTML content.
        :type value: string, optional
        """
        self._value = None
        self._validator = ValidateAPIKey()

        if value is not None:
            self.value = value

    @property
    def type(self):
        """The actual text content.

        :rtype: string
        """
        return "text/html"

    @property
    def value(self):
        """The actual HTML content.

        :rtype: string
        """
        return self._value

    @value.setter
    def value(self, value):
        self._validator.validate_message_dict(value)
        self._value = value

    def get(self):
        """
        Get a JSON-ready representation of this HtmlContent.

        :returns: This HtmlContent, ready for use in a request body.
        :rtype: dict
        """
        content = {}
        content["type"] = self.type
        content["value"] = self.value
        return content
