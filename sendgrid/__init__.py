"""
This library allows you to quickly and easily use the SendGrid Web API v3 via
Python.

For more information on this library, see the README on Github.
    http://github.com/sendgrid/sendgrid-python
For more information on the SendGrid v3 API, see the v3 docs:
    http://sendgrid.com/docs/API_Reference/api_v3.html
For the user guide, code examples, and more, visit the main docs page:
    http://sendgrid.com/docs/index.html

Available subpackages
---------------------
helpers
    Modules to help with common tasks.
"""

import os
# v3 API
from .sendgrid import SendGridAPIClient  # noqa
from .helpers.mail import Email  # noqa


dir_path = os.path.dirname(os.path.realpath(__file__))
if os.path.isfile(os.path.join(dir_path, 'VERSION.txt')):
    __version__ = open(os.path.join(dir_path, 'VERSION.txt')).read().strip()
