import io
import sys
import json
try:
    import rfc822
except Exception as e:
    import email.utils as rfc822
from smtpapi import SMTPAPIHeader


class Mail():

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
        self.reply_to = ''
        self.set_replyto(opts.get('reply_to', ''))
        self.files = opts.get('files', {})
        self.headers = {}
        self.set_headers(opts.get('headers', {}))
        self.date = opts.get('date', rfc822.formatdate())
        self.content = opts.get('content', {})
        self.smtpapi = opts.get('smtpapi', SMTPAPIHeader())

    def parse_and_add(self, to):
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
        elif type(to) is tuple:
            if len(to) == 1:
                self.add_to(to[0])
            elif len(to) == 2:
                self.add_to(to[0])
                self.add_to_name(to[1])
        elif hasattr(to, '__iter__'):
            for email in to:
                self.add_to(email)

    def add_to_name(self, to_name):
        if isinstance(to_name, str):
            self.to_name.append(to_name)
        elif sys.version_info < (3, 0) and isinstance(to_name, unicode):
            self.to_name.append(to_name.encode('utf-8'))
        elif hasattr(to_name, '__iter__'):
            for tn in to_name:
                self.add_to_name(tn)

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
        name, email = rfc822.parseaddr(replyto.replace(',', ''))
        if name and email:
            self.set_reply_to_name(replyto)
        elif email:
            self.reply_to = email

    def set_reply_to_name(self, replyto):
        headers = {
            "Reply-To":  replyto
        }
        self.reply_to = ''
        self.set_headers(headers)

    def add_attachment(self, name, file_):
        if sys.version_info < (3, 0) and isinstance(name, unicode):
            name = name.encode('utf-8')
        if isinstance(file_, str):  # filepath
            with open(file_, 'rb') as f:
                self.files[name] = f.read()
        elif hasattr(file_, 'read'):
            self.files[name] = file_.read()

    def add_attachment_stream(self, name, string):
        if sys.version_info < (3, 0) and isinstance(name, unicode):
            name = name.encode('utf-8')
        if isinstance(string, io.BytesIO):
            self.files[name] = string.read()
        else:
            self.files[name] = string

    def add_content_id(self, cid, value):
        self.content[cid] = value

    def set_headers(self, headers):
        if sys.version_info < (3, 0) and isinstance(headers, unicode):
            headers = headers.encode('utf-8')
        if isinstance(self.headers, str):
            self.headers = json.loads(self.headers)
        if isinstance(headers, str):
            headers = json.loads(headers)
        for key, value in headers.items():
            self.headers[key] = value

    def set_date(self, date):
        self.date = date

    # SMTPAPI Wrapper methods

    def add_substitution(self, key, value):
        self.smtpapi.add_substitution(key, value)

    def set_substitutions(self, subs):
        self.smtpapi.set_substitutions(subs)

    def add_unique_arg(self, key, value):
        self.smtpapi.add_unique_arg(key, value)

    def set_unique_args(self, args):
        self.smtpapi.set_unique_args(args)

    def add_category(self, cat):
        self.smtpapi.add_category(cat)

    def set_categories(self, cats):
        self.smtpapi.set_categories(cats)

    def add_section(self, key, value):
        self.smtpapi.add_section(key, value)

    def set_sections(self, sections):
        self.smtpapi.set_sections(sections)

    def add_filter(self, filterKey, setting, value):
        self.smtpapi.add_filter(filterKey, setting, value)

    def set_asm_group_id(self, value):
        self.smtpapi.set_asm_group_id(value)

    def json_string(self):
        return self.smtpapi.json_string()
