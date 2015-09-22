import sys
import json
from socket import timeout
from .version import __version__
try:
    import urllib.request as urllib_request
    from urllib.parse import urlencode
    from urllib.error import HTTPError
except ImportError:  # Python 2
    import urllib2 as urllib_request
    from urllib2 import HTTPError
    from urllib import urlencode

from .exceptions import SendGridClientError, SendGridServerError


class SendGridClient(object):

    """SendGrid API."""

    def __init__(self, username_or_apikey, password=None, **opts):
        """
        Construct SendGrid API object.

        Args:
            username: SendGrid username
            password: SendGrid password
            user: Send mail on behalf of this user (web only)
            raise_errors: If set to False (default): in case of error, `.send`
                method will return a tuple (http_code, error_message). If set
                to True: `.send` will raise SendGridError. Note, from version
                1.0.0, the default will be changed to True, so you are
                recommended to pass True for forwards compatability.
        """

        # Check if username + password or api key
        if password is None:
            # API Key
            self.username = None
            self.password = username_or_apikey
        else:
            # Username + password
            self.username = username_or_apikey
            self.password = password

        self.useragent = 'sendgrid/' + __version__ + ';python'
        self.host = opts.get('host', 'https://api.sendgrid.com')
        self.port = str(opts.get('port', '443'))
        self.endpoint = opts.get('endpoint', '/api/mail.send.json')
        self.mail_url = self.host + ':' + self.port + self.endpoint
        self._raise_errors = opts.get('raise_errors', False)
        # urllib cannot connect to SSL servers using proxies
        self.proxies = opts.get('proxies', None)

    def _build_body(self, message):
        if sys.version_info < (3, 0):
            ks = ['from_email', 'from_name', 'subject',
                  'text', 'html', 'reply_to']
            for k in ks:
                v = getattr(message, k)
                if isinstance(v, unicode):
                    setattr(message, k, v.encode('utf-8'))

        values = {
            'to[]': message.to if message.to else [message.from_email],
            'toname[]': message.to_name,
            'cc[]': message.cc,
            'bcc[]': message.bcc,
            'from': message.from_email,
            'fromname': message.from_name,
            'subject': message.subject,
            'text': message.text,
            'html': message.html,
            'replyto': message.reply_to,
            'headers': json.dumps(message.headers) if message.headers else '',
            'date': message.date,
            'x-smtpapi': message.json_string()
        }

        if self.username != None:
            # Using username + password
            values['api_user'] = self.username
            values['api_key'] = self.password

        for k in list(values.keys()):
            if not values[k]:
                del values[k]
        for filename in message.files:
            if message.files[filename]:
                values['files[' + filename + ']'] = message.files[filename]
        for content in message.content:
            if message.content[content]:
                values['content[' + content + ']'] = message.content[content]
        return values

    def _make_request(self, message):
        if self.proxies:
            proxy_support = urllib_request.ProxyHandler(self.proxies)
            opener = urllib_request.build_opener(proxy_support)
            urllib_request.install_opener(opener)
        data = urlencode(self._build_body(message), True).encode('utf-8')
        req = urllib_request.Request(self.mail_url, data)
        req.add_header('User-Agent', self.useragent)

        if self.username is None:
            # Using API key
            req.add_header('Authorization', 'Bearer ' + self.password)

        response = urllib_request.urlopen(req, timeout=10)
        body = response.read()
        return response.getcode(), body

    def send(self, message):
        if self._raise_errors:
            return self._raising_send(message)
        else:
            return self._legacy_send(message)

    def _legacy_send(self, message):
        try:
            return self._make_request(message)
        except HTTPError as e:
            return e.code, e.read()
        except timeout as e:
            return 408, e

    def _raising_send(self, message):
        try:
            return self._make_request(message)
        except HTTPError as e:
            if 400 <= e.code < 500:
                raise SendGridClientError(e.code, e.read())
            elif 500 <= e.code < 600:
                raise SendGridServerError(e.code, e.read())
            else:
                assert False
        except timeout as e:
            raise SendGridClientError(408, 'Request timeout')
