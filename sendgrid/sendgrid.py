import sys
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
        self.mail_url = 'https://api.sendgrid.com/api/mail.send.json'

        # urllib cannot connect to SSL servers using proxies
        self.proxies = opts.get('proxies', None)

    def _build_body(self, message):
        values = {
            'api_user': self.username,
            'api_key': self.password,
            'to[]': message.to,
            'toname[]': message.to_name,
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
        for filename in message.files:
            values['files[' + filename + ']'] = message.files[filename]
        if sys.hexversion < 0x03000000:
            # python 2
            values = dict((k, v) for k, v in values.iteritems() if v)
        else:
            # python 3
            values = dict((k, v) for k, v in values.items() if v)
        return values

    def send(self, message):
        try:
            if self.proxies:
                proxy_support = urllib_request.ProxyHandler(self.proxies)
                opener = urllib_request.build_opener(proxy_support)
                urllib_request.install_opener(opener)
            data = urlencode(
                self._build_body(message),
                True).encode('utf-8')
            req = urllib_request.Request(self.mail_url, data)
            response = urllib_request.urlopen(req)
            body = response.read()
            return response.getcode(), body
        except URLError as e:
            return e.code, e.read()
