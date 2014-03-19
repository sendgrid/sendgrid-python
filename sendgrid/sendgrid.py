import sys
from socket import timeout
try:
    import urllib.request as urllib_request
    from urllib.parse import urlencode
    from urllib.error import URLError
except ImportError: # Python 2
    import urllib2 as urllib_request
    from urllib2 import URLError
    from urllib import urlencode

class SendGridClient(object):

    """SendGrid API."""

    def __init__(self, username, password, **opts):
        """
        Construct SendGrid API object.

        Args:
            username: SendGrid username
            password: SendGrid password
            user: Send mail on behalf of this user (web only)

        """
        self.username = username
        self.password = password
        self.host = opts.get('host', 'https://api.sendgrid.com')
        self.port = opts.get('port', '443')
        self.endpoint = '/api/mail.send.json'
        self.mail_url = self.host + ':' + self.port + self.endpoint
        # urllib cannot connect to SSL servers using proxies
        self.proxies = opts.get('proxies', None)

    def _build_body(self, message):
        if sys.version_info < (3,0):
            message.from_email = message.from_email.encode('utf-8')
            message.from_name = message.from_name.encode('utf-8')
            message.subject = message.subject.encode('utf-8')
            message.text = message.text.encode('utf-8')
            message.html = message.html.encode('utf-8')
            message.reply_to = message.reply_to.encode('utf-8')


        values = {
            'api_user': self.username,
            'api_key': self.password,
            'to[]': message.to,
            'toname[]': message.to_name,
            'bcc[]': message.bcc,
            'from': message.from_email,
            'fromname': message.from_name,
            'subject': message.subject,
            'text': message.text,
            'html': message.html,
            'replyto': message.reply_to,
            'headers': message.headers,
            'date': message.date,
            'x-smtpapi': message.json_string()
        }
        for k in list(values.keys()):
            if not values[k]:
                del values[k]
        for filename in message.files:
            if message.files[filename]:
                values['files[' + filename + ']'] = message.files[filename]
        return values

    def send(self, message):
        try:
            if self.proxies:
                proxy_support = urllib_request.ProxyHandler(self.proxies)
                opener = urllib_request.build_opener(proxy_support)
                urllib_request.install_opener(opener)
            data = urlencode(self._build_body(message), True).encode('utf-8')
            req = urllib_request.Request(self.mail_url, data)
            response = urllib_request.urlopen(req, timeout = 10)
            body = response.read()
            return response.getcode(), body
        except URLError as e:
            return e.code, e.read()
        except timeout as e:
            return 408, e
