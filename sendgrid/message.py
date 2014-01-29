import io
try:
  import rfc822
except Exception as e:
  import email.utils as rfc822

from smtpapi import SMTPAPIHeader


class Mail(SMTPAPIHeader):
  """
  Sendgrid Message
  """

  def __init__(self, **opts):
    """
    Constructs Sendgrid Message object

    Args:
      to: Receipient
      to_name: Receipient name
      from: Sender
      subject: Email title
      text: Email body
      html: Email body
      bcc: Receipient
      reply_to: Reply address
      date: Set date
      headers: Set headers
      x-smtpapi: Set SG custom header
      files: Attachments

    """
    super(Mail, self).__init__()
    self.to = opts.get('to', [])
    self.to_name = opts.get('to_name', [])
    self.from_name = opts.get('from', '')
    self.subject = opts.get('subject', '')
    self.text = opts.get('text', '')
    self.html = opts.get('html', '')
    self.bcc = opts.get('bcc', [])
    self.reply_to = opts.get('reply_to', '')
    self.files = opts.get('files', {})
    self.headers = opts.get('headers', '')
    self.date = opts.get('date', rfc822.formatdate())

  def add_to(self, to):
    name, email = rfc822.parseaddr(to.replace(',', ''))
    if email:
      self.to.append(email)
    if name:
      self.add_to_name(name);

  def add_to_name(self, to_name):
    self.to_name.append(to_name)

  def set_from(self, from_name):
    self.from_name = from_name

  def set_subject(self, subject):
    self.subject = subject

  def set_text(self, text):
    self.text = text

  def set_html(self, html):
    self.html = html

  def add_bcc(self, bcc):
    self.bcc.append(bcc)

  def set_replyto(self, replyto):
    self.reply_to = replyto

  def add_attachment(self, name, filepath):
    self.files[name] = open(filepath, "r").read()

  def add_attachment_stream(self, name, string):
    if isinstance(string, str):
      self.files[name] = string
    elif isinstance(string, io.BytesIO):
      self.files[name] = string.read()

  def set_headers(self, headers):
    self.headers = headers

  def set_date(self, date):
    self.date = date
