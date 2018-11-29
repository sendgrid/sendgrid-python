from .content import Content
from .validators import ValidateAPIKey


class PlainTextContent(Content):
    """Plain text content to be included in your email.
    """

    def __init__(self, value, validator=None):
        """Create a PlainTextContent with the specified MIME type and value.

        :param value: The actual text content.
        """
        self._value = None
        self._validator = None

        if value is not None:
            self.value = value
        if validator is not None:
            self.validator = validator
        else:
            self.validator = ValidateAPIKey()

    @property
    def type(self):
        """The actual text content.

        :rtype: string
        """
        return "text/plain"

    @property
    def value(self):
        """The actual text content.

        :rtype: string
        """
        return self._value

    @value.setter
    def value(self, value):
        self.validator.validate_message_dict(value)
        self._value = value

    @property
    def validator(self):
        return self._validator

    @validator.setter
    def validator(self, value):
        self._validator = value

    def get(self):
        """
        Get a JSON-ready representation of this PlainTextContent.

        :returns: This PlainTextContent, ready for use in a request body.
        :rtype: dict
        """
        content = {}
        content["type"] = self.type
        content["value"] = self.value
        return content
