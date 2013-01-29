try:
    import json
except ImportError:
    import simplejson as json


class SmtpApiHeader(object):
    def __init__(self):
        self.data = {}

    def add_to(self, to):
        if 'to' not in self.data:
            self.data['to'] = []
        if type(to) is str:
            self.data['to'] += [to]
        else:
            self.data['to'] += to

    def add_cc(self, cc):
        if 'cc' not in self.data:
            self.data['cc'] = []
        if type(cc) is str:
            self.data['cc'] += [cc]
        else:
            self.data['cc'] += cc

    def add_bcc(self, bcc):
        if 'bcc' not in self.data:
            self.data['bcc'] = []
        if type(bcc) is str:
            self.data['bcc'] += [bcc]
        else:
            self.data['bcc'] += bcc

    def set_replyto(self, replyto):
        self.data['reply_to'] = replyto

    def add_sub_val(self, var, val):
        if 'sub' not in self.data:
            self.data['sub'] = {}
        if type(val) is str:
            self.data['sub'][var] = [val]
        else:
            self.data['sub'][var] = val

    def set_unique_args(self, val):
        if type(val) is dict:
            self.data['unique_args'] = val

    def add_unique_arg(self, key, val):
        if 'unique_args' not in self.data:
            self.data['unique_args'] = {}
        self.data['unique_args'][key] = val

    def set_category(self, cat):
        self.data['category'] = [cat]

    def add_category(self, cat):
        if 'category' not in self.data:
            self.data['category'] = []
        self.data['category'].append(cat)

    def add_section(self, key, section):
        if 'section' not in self.data:
            self.data['section'] = {}
        self.data['section'][key] = section

    def set_section(self, val):
        self.data['section'] = val

    def add_filter_setting(self, fltr, setting, val):
        if 'filters' not in self.data:
            self.data['filters'] = {}
        if fltr not in self.data['filters']:
            self.data['filters'][fltr] = {}
        if 'settings' not in self.data['filters'][fltr]:
            self.data['filters'][fltr]['settings'] = {}
        self.data['filters'][fltr]['settings'][setting] = val

    def as_json(self):
        return json.dumps(self.data)

    def as_string(self):
        str = 'X-SMTPAPI: %s' % self.as_json()
        return str
