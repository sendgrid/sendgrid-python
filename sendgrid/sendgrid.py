import requests

class SendGridClient(object):
    """
    SendGrid API
    """
    def __init__(self, username, password, **opts):
        """
        Construct Sendgrid API object

        Args:
            username: Sendgrid username
            password: Sendgrid password
            user: Send mail on behalf of this user (web only)
        """
        self.username = username
        self.password = password
        self.mailUrl = 'https://api.sendgrid.com/api/mail.send.json'
        self.proxies = opts.get('proxies', None)

    def send(self, message):
      values = {}
      values['api_user'] = self.username
      values['api_key'] = self.password
      values['to[]'] = message.to
      values['to_name[]'] = message.to_name
      values['from'] = message.from_name
      values['subject'] = message.subject
      values['text'] = message.text
      values['html'] = message.html
      values['reply_to'] = message.reply_to
      values['headers'] = message.headers
      values['date'] = message.date
      for filename in message.files:
        values['files[' + filename + ']'] = message.files[filename]
      values['x-smtpapi'] = str(message.json_string())
      r = requests.get(self.mailUrl, params=values, proxies=self.proxies)
      return r.status_code, r.json()
