"""
This library allows you to quickly and easily use the SendGrid Web API v3 via
Python.  For more information, see the README on Github.

http://github.com/sendgrid/sendgrid-python

Available subpackages
---------------------
helpers
    Modules to help with common tasks.
"""

from .version import __version__  # noqa
# v3 API
from .sendgrid import SendGridAPIClient  # noqa
from .helpers.mail.mail import Email  # noqa
