import rfc822
import base64
from header import SMTPAPIHeader


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
        self.from_name = opts.get('from', None)
        self.subject = opts.get('subject', None)
        self.text = opts.get('text', None)
        self.html = opts.get('html', None)
        self.bcc = opts.get('bcc', [])
        self.reply_to = opts.get('reply_to', None)
        self.files = opts.get('files', {})
        self.headers = opts.get('headers', None)
        self.date = opts.get('date', rfc822.formatdate())

    def add_to(self, to):
        """
        Add recipient

        Args:
          to: email str or list of email str(s)
        """
        if isinstance(to, (str, unicode)):
            self.to.append(to)
        elif isinstance(to, list):
            self.to += to

    def add_to_name(self, to_name):
        if isinstance(to_name, (str, unicode)):
            self.to_name.append(to_name)
        elif isinstance(to_name, list):
            self.to_name += to_name

    def set_from(self, from_name):
        self.from_name = from_name


    def set_subject(self, subject):
        self.subject = subject

    def set_text(self, text):
        self.text = text

    def set_html(self, html):
        self.html = html

    def add_bcc(self, bcc):
        """
        Add BCC recipients

        Args:
          to: email str or list of email str(s)
        """
        if isinstance(bcc, (str, unicode)):
            self.bcc.append(bcc)
        elif isinstance(bcc, list):
            self.bcc += bcc

    def set_replyto(self, replyto):
        """
        Set a Reply-To: address for the outgoing message

        Args:
            replyto: reply address, accepts string

        """
        self.reply_to = replyto

    def add_attachment(self, name, filepath):
        """
        Add attachment to email

        Args:
            name: name of the file as seen in email
            file: path to file or data string

        """
        self.files[name] = base64.urlsafe_b64encode(open(filepath, "rb").read())

    def set_headers(self, headers):
        self.headers = headers

    def set_date(self, date):
        self.date = date
