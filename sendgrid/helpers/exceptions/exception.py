
"""
    Exceptions: custom SendGrid related exceptions
"""

class SendGridException(Exception):
    """
        Wrapper/default SendGrid-related exception
    """

    pass


class APIKeyIncludedException(SendGridException):
    """
        SendGrid API Key included in message text
    """

    pass
