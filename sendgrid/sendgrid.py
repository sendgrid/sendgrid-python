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

    def __init__(
            self,
            apikey=None,
            api_key=None,
            impersonate_subuser=None,
            host='https://api.sendgrid.com'):
        """
        Construct SendGrid v3 API object.

        :param apikey: SendGrid API key to use. If not provided, key will be read from
            environment variable "SENDGRID_API_KEY"
        :type apikey: basestring
        :param api_key: SendGrid API key to use. Provides backward compatibility
            .. deprecated:: 5.3
                Use apikey instead
        :type api_key: basestring
        :param impersonate_subuser: the subuser to impersonate. Will be passed by
            "On-Behalf-Of" header by underlying client.
            See https://sendgrid.com/docs/User_Guide/Settings/subusers.html for more details
        :type impersonate_subuser: basestring
        :param host: base URL for API calls
        :type host: basestring
        """
        self._apikey = apikey or api_key or os.environ.get('SENDGRID_API_KEY')
        self._impersonate_subuser = impersonate_subuser
        self.host = host
        self.useragent = 'sendgrid/{0};python'.format(__version__)
        self.version = __version__

        self.client = python_http_client.Client(host=self.host,
                                                request_headers=self._default_headers,
                                                version=3)

    @property
    def _default_headers(self):
        headers = {
            "Authorization": 'Bearer {0}'.format(self._apikey),
            "User-agent": self.useragent,
            "Accept": 'application/json'
        }
        if self._impersonate_subuser:
            headers['On-Behalf-Of'] = self._impersonate_subuser

        return headers

    def reset_request_headers(self):
        self.client.request_headers = self._default_headers

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
