"""
This library allows you to quickly and easily use the SendGrid Web API v3 via
Python.

For more information on this library, see the README on Github.
    http://github.com/sendgrid/sendgrid-python
For more information on the SendGrid v3 API, see the v3 docs:
    http://sendgrid.com/docs/API_Reference/api_v3.html
For the user guide, code examples, and more, visit the main docs page:
    http://sendgrid.com/docs/index.html

This file provides the SendGrid API Client.
"""


import os
import python_http_client

from .version import __version__


class SendGridAPIClient(object):
    """The SendGrid API Client.

    Use this object to interact with the v3 API.  For example:
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        ...
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())

    For examples and detailed use instructions, see
        https://github.com/sendgrid/sendgrid-python
    """

    def __init__(self, **opts):
        """
        Construct SendGrid v3 API object.

        :params host: Base URL for the API call
        :type host: string
        :params apikey: SendGrid API key to use.  Defaults to environment var.
        :type apikey: string
        """
        self.path = opts.get(
            'path', os.path.abspath(os.path.dirname(__file__)))
        self._apikey = opts.get('apikey', os.environ.get('SENDGRID_API_KEY'))
        # Support v2 api_key naming
        self._apikey = opts.get('api_key', self._apikey)
        self._api_key = self._apikey
        # Support impersonation of subusers
        self._impersonate_subuser = opts.get('impersonate_subuser', None)
        self.useragent = 'sendgrid/{0};python'.format(__version__)
        self.host = opts.get('host', 'https://api.sendgrid.com')
        self.version = __version__

        headers = self._get_default_headers()

        self.client = python_http_client.Client(host=self.host,
                                                request_headers=headers,
                                                version=3)

    def _get_default_headers(self):
        headers = {
            "Authorization": 'Bearer {0}'.format(self._apikey),
            "User-agent": self.useragent,
            "Accept": 'application/json'
        }
        if self._impersonate_subuser:
            headers['On-Behalf-Of'] = self._impersonate_subuser

        return headers

    def reset_request_headers(self):
        self.client.request_headers = self._get_default_headers()

    @property
    def apikey(self):
        """The API key (also accessible as api_key)."""
        return self._apikey

    @apikey.setter
    def apikey(self, value):
        self._apikey = value

    @property
    def api_key(self):
        """The API key (also accessible as apikey)."""
        return self._apikey

    @api_key.setter
    def api_key(self, value):
        self._apikey = value

    @property
    def impersonate_subuser(self):
        """
        The subuser you are impersonating.

        If present, this is the value of the "On-Behalf-Of" header.
        """
        return self._impersonate_subuser
