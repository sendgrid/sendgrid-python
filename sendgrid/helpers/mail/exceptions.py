################################################################
# Various types of extensible SendGrid related exceptions
################################################################


class SendGridException(Exception):
    """Wrapper/default SendGrid-related exception"""
    pass


class APIKeyIncludedException(SendGridException):
    """Exception raised for when SendGrid API Key included in message text"""

    def __init__(self,
                 expression="Email body",
                 message="SendGrid API Key detected"):
        """Create an exception for when SendGrid API Key included in message text
        
            :param expression: Input expression in which the error occurred
            :type expression: string
            :param message: Explanation of the error
            :type message: string
        """
        self._expression = None
        self._message = None

        if expression is not None:
            self.expression = expression

        if message is not None:
            self.message = message

    @property
    def expression(self):
        """Input expression in which the error occurred

        :rtype: string
        """
        return self._expression

    @expression.setter
    def expression(self, value):
        self._expression = value

    @property
    def message(self):
        """Explanation of the error

        :rtype: string
        """
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
