import urllib
import urllib2
try:
    import json
except ImportError:
    import simplejson as json


from sendgrid import exceptions


class Http(object):
    """
    Transport to send emails using http
    """
    HOSTPORT = ('sendgrid.com',)

    def __init__(self, username, password, **opts):
        """
        Construct web transport object

        Args:
            username: Sendgrid username
            password: Sendgrid password
            ssl: Use SSL
            user: Send mail on behalf of this user
        """
        self.username = username
        self.password = password
        self.ssl = opts.get('ssl', True)
        self.user = opts.get('user', None)

    def send(self, message):
        """
        Send message

        Args:
            message: Sendgrid Message object

        Returns:
            True on success

        Raises:
            SGServiceException: on error
        """
        protocol = "https://"
        if not self.ssl:
            protocol = "http://"
        endpoint = "/api/mail.send.json"

        url = protocol + ":".join(map(str, self.HOSTPORT)) + endpoint

        data = {
            'api_user': self.username,
            'api_key': self.password,
            'to': message.to,
            'subject': message.subject,
            'from': message.from_address,
            'date': message.date,
            }

        if message.header.data:
            data['x-smtpapi'] = message.header.as_json()
        if message.headers:
            data['headers'] = json.dumps(message.headers)
        if message.attachments:
            for attach in message.attachments:
                try:
                    f = open(attach['file'], 'rb')
                    data['files[' + attach['name'] + ']'] = f.read()
                    f.close()
                except IOError:
                    data['files[' + attach['name'] + ']'] = attach['file']

        optional_params = {
            'toname': message.to_name,
            'text': message.text,
            'html': message.html,
            'cc': message.cc,  # for future use, not yet implemented
            'bcc': message.bcc,
            'fromname': message.from_name,
            'replyto': message.reply_to,
            'user': self.user,
            }

        for key in optional_params:
            if optional_params[key]:
                data[key] = optional_params[key]

        data = urllib.urlencode(data, 1)
        req = urllib2.Request(url, data)
        try:
            f = urllib2.urlopen(req)
            output = f.read()
        except IOError, e:
            try:
                output = e.read()
            except AttributeError:
                raise exceptions.SGServiceException(e)

        output = json.loads(output)

        if output['message'] == 'error':
            raise exceptions.SGServiceException(output['errors'])

        return True

