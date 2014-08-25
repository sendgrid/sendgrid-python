import io
import sys
try:
    import rfc822
except Exception as e:
    import email.utils as rfc822
from smtpapi import SMTPAPIHeader


class Mail(SMTPAPIHeader):

    """SendGrid Message."""

    def __init__(self, **opts):
        """
        Constructs SendGrid Message object.

        Args:
            to: Recipient
            to_name: Recipient name
            from_email: Sender email
            from_name: Sender name
            subject: Email title
            text: Email body
            html: Email body
            bcc: Recipient
            reply_to: Reply address
            date: Set date
            headers: Set headers
            files: Attachments
        """
        super(Mail, self).__init__()
        self.to = []
        self.to_name = []
        self.cc = []
        self.add_to(opts.get('to', []))
        self.add_to_name(opts.get('to_name', []))
        self.add_cc(opts.get('cc', []))
        self.from_email = opts.get('from_email', '')
        self.from_name = opts.get('from_name', '')
        self.subject = opts.get('subject', '')
        self.text = opts.get('text', '')
        self.html = opts.get('html', '')
        self.bcc = []
        self.add_bcc(opts.get('bcc', []))
        self.reply_to = opts.get('reply_to', '')
        self.files = opts.get('files', {})
        self.headers = opts.get('headers', '')
        self.date = opts.get('date', rfc822.formatdate())
        self.content = opts.get('content', {})

    def parse_and_add(self, to):
        super(Mail, self).add_to(to)
        name, email = rfc822.parseaddr(to.replace(',', ''))
        if email:
            self.to.append(email)
        if name:
            self.add_to_name(name)

    def add_to(self, to):
        if isinstance(to, str):
            self.parse_and_add(to)
        elif sys.version_info < (3, 0) and isinstance(to, unicode):
            self.parse_and_add(to.encode('utf-8'))
        elif hasattr(to, '__iter__'):
            for email in to:
                self.add_to(email)

    def add_to_name(self, to_name):
        if isinstance(to_name, str):
            self.to_name.append(to_name)
        elif sys.version_info < (3, 0) and isinstance(to_name, unicode):
            self.to_name.append(to_name.encode('utf-8'))
        elif hasattr(to_name, '__iter__'):
            self.to_name = self.to_name + to_name

    def add_cc(self, cc):
        if isinstance(cc, str):
            email = rfc822.parseaddr(cc.replace(',', ''))[1]
            self.cc.append(email)
        elif sys.version_info < (3, 0) and isinstance(cc, unicode):
            email = rfc822.parseaddr(cc.replace(',', ''))[1].encode('utf-8')
            self.cc.append(email)
        elif hasattr(cc, '__iter__'):
            for email in cc:
                self.add_cc(email)

    def set_from(self, from_email):
        name, email = rfc822.parseaddr(from_email.replace(',', ''))
        if email:
            self.from_email = email
        if name:
            self.set_from_name(name)

    def set_from_name(self, from_name):
        self.from_name = from_name

    def set_subject(self, subject):
        self.subject = subject

    def set_text(self, text):
        self.text = text

    def set_html(self, html):
        self.html = html

    def add_bcc(self, bcc):
        if isinstance(bcc, str):
            email = rfc822.parseaddr(bcc.replace(',', ''))[1]
            self.bcc.append(email)
        elif sys.version_info < (3, 0) and isinstance(bcc, unicode):
            email = rfc822.parseaddr(bcc.replace(',', ''))[1].encode('utf-8')
            self.bcc.append(email)
        elif hasattr(bcc, '__iter__'):
            for email in bcc:
                self.add_bcc(email)

    def set_replyto(self, replyto):
        self.reply_to = replyto

    def add_attachment(self, name, file_):
        if isinstance(file_, str):  # filepath
            with open(file_, 'rb') as f:
                self.files[name] = f.read()
        elif hasattr(file_, 'read'):
            self.files[name] = file_.read()

    def add_attachment_stream(self, name, string):
        if isinstance(string, str):
            self.files[name] = string
        elif isinstance(string, io.BytesIO):
            self.files[name] = string.read()
        elif sys.version_info < (3, 0) and isinstance(string, unicode):
            self.files[name] = string

    def add_content_id(self, cid, value):
        self.content[cid] = value

    def set_headers(self, headers):
        self.headers = headers

    def set_date(self, date):
        self.date = date
