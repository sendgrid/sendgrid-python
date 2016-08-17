"""Parse data received from the SendGrid Inbound Parse webhook"""
import base64
import email
import mimetypes
from werkzeug.utils import secure_filename

class Parse(object):
    def __init__(self, config, request):
        self._keys = config.keys
        self._request = request
        request.get_data(as_text=True)
        self._payload = request.form
        self._raw_payload = request.data

    """Return a dictionary of key/values in the payload received from the webhook"""
    def key_values(self):
        key_values = {}
        for key in self.keys:
            if key in self.payload:
                key_values[key] = self.payload[key]
        return key_values

    """This only applies to raw payloads:
    https://sendgrid.com/docs/Classroom/Basics/Inbound_Parse_Webhook/setting_up_the_inbound_parse_webhook.html#-Raw-Parameters"""
    def get_raw_email(self):
        if 'email' in self.payload:
            raw_email = email.message_from_string(self.payload['email'])
            return raw_email
        else:
            return None

    """Returns an object with:
    type = file content type
    file_name = the name of the file
    contents = base64 encoded file contents"""
    def attachments(self):
        attachments = []
        if 'attachment-info' in self.payload:
            for _, filestorage in self.request.files.iteritems():
                attachment = {}
                if filestorage.filename not in (None, 'fdopen', '<fdopen>'):
                    filename = secure_filename(filestorage.filename)
                    attachment['type'] = filestorage.content_type
                    attachment['file_name'] = filename
                    attachment['contents'] = base64.b64encode(filestorage.getvalue())
                    attachments.append(attachment)
            return attachments

        # Check if we have a raw message
        attachments = []
        raw_email = self.get_raw_email()
        if raw_email != None:
            counter = 1
            for part in raw_email.walk():
                attachment = {}
                if part.get_content_maintype() == 'multipart':
                    continue
                filename = part.get_filename()
                if not filename:
                    ext = mimetypes.guess_extension(part.get_content_type())
                    if not ext:
                        ext = '.bin'
                    filename = 'part-%03d%s' % (counter, ext)
                counter += 1
                attachment['type'] = part.get_content_type()
                attachment['filename'] = filename
                attachment['contents'] = part.get_payload(decode=False)
                attachments.append(attachment)
            return attachments
        return None

    @property
    def keys(self):
        return self._keys

    @property
    def request(self):
        return self._request

    @property
    def payload(self):
        return self._payload

    @property
    def raw_payload(self):
        return self._raw_payload