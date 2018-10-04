from .content import Content
from .validators import ValidateAPIKey


class HtmlContent(Content):
    """HTML content to be included in your email."""

    def __init__(self, value):
        """Create an HtmlContent with the specified MIME type and value.

        :param value: The HTML content.
        :type value: string, optional
        """
        self._validator = ValidateAPIKey()
        self.type = "text/html"
        self.value = value

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
        content["type"] = "text/html"
        content["value"] = self._value
        return content
