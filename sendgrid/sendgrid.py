import sys
if sys.hexversion < 0x03000000:
    # python 2
    import urllib
    import urllib2
else:
    # python 3
    import urllib.parse
    import urllib.request


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
        return values

    def send(self, message):
        if sys.hexversion < 0x03000000:
            # python 2
            try:
                if self.proxies:
                    proxy_support = urllib2.ProxyHandler(self.proxies)
                    opener = urllib2.build_opener(proxy_support)
                    urllib2.install_opener(opener)
                data = urllib.urlencode(
                    self._build_body(message),
                    True).encode('utf-8')
                req = urllib2.Request(self.mail_url, data)
                response = urllib2.urlopen(req)
                body = response.read()
                return response.getcode(), body
            except urllib2.URLError as e:
                raise e

        else:
            # python 3
            try:
                if self.proxies:
                    proxy_support = urllib.request.ProxyHandler(self.proxies)
                    opener = urllib.request.build_opener(proxy_support)
                    urllib.request.install_opener(opener)
                data = urllib.parse.urlencode(
                    self._build_body(message),
                    True).encode('utf-8')
                req = urllib.request.Request(self.mail_url, data)
                response = urllib.request.urlopen(req)
                body = response.read()
                return response.getcode(), body
            except urllib.error.URLError as e:
                raise e
