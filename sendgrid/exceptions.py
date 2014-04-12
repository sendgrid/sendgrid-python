class SendGridError(Exception):

    """Base class for SendGrid-related errors."""


class SendGridClientError(SendGridError):

    """Client error, which corresponds to a 4xx HTTP error."""


class SendGridServerError(SendGridError):

    """Server error, which corresponds to a 5xx HTTP error."""
