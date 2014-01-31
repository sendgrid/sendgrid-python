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

  def _build_url(self, message):
    values = {}
    values['api_user'] = self.username
    values['api_key'] = self.password
    values['to[]'] = message.to
    values['toname[]'] = message.to_name
    values['from'] = message.from_email
    values['from_name'] = message.from_name
    values['subject'] = message.subject
    values['text'] = message.text
    values['html'] = message.html
    values['replyto'] = message.reply_to
    values['headers'] = message.headers
    values['date'] = message.date
    for filename in message.files:
      values['files[' + filename + ']'] = message.files[filename]
    values['x-smtpapi'] = message.json_string()
    return values

  def send(self, message):
    try:
      r = requests.get(self.mailUrl, params=self._build_url(message), proxies=self.proxies)
      return r.status_code, r.json()
    except requests.exceptions.ConnectionError as e:
      raise e
