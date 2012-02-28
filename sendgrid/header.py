try:
    import json
except ImportError:
    import simplejson as json
import re
import textwrap

class SmtpApiHeader(object):
    def __init__(self):
        self.data = {}
        self.re_split = re.compile('(["\]}])([,:])(["\[{])')


    def add_to(self, to):
        if not self.data.has_key('to'):
            self.data['to'] = []
        if type(to) is str:
            self.data['to'] += [to]
        else:
            self.data['to'] += to


    def add_sub_val(self, var, val):
        if not self.data.has_key('sub'):
            self.data['sub'] = {}
        if type(val) is str:
            self.data['sub'][var] = [val]
        else:
            self.data['sub'][var] = val


    def set_unique_args(self, val):
        if type(val) is dict:
            self.data['unique_args'] = val


    def add_unique_arg(self, key, val):
        if not self.data.has_key('unique_args'):
            self.data['unique_args'] = {}
        self.data['unique_args'][key] = val


    def set_category(self, cat):
        self.data['category'] = [cat]


    def add_category(self, cat):
        if not self.data.has_key('category'):
            self.data['category'] = []
        self.data['category'].append(cat)


    def add_section(self, key, section):
        if not self.data.has_key('section'):
            self.data['section'] = {}
        self.data['section'][key] = section


    def set_section(self, val):
        self.data['section'] = val


    def add_filter_setting(self, fltr, setting, val):
        if not self.data.has_key('filters'):
            self.data['filters'] = {}
        if not self.data['filters'].has_key(fltr):
            self.data['filters'][fltr] = {}
        if not self.data['filters'][fltr].has_key('settings'):
            self.data['filters'][fltr]['settings'] = {}
        self.data['filters'][fltr]['settings'][setting] = val


    def as_json(self):
        j = json.dumps(self.data)
        return self.re_split.sub('\1\2 \3', j)


    def as_string(self):
        j = self.as_json()
        str = 'X-SMTPAPI: %s' % textwrap.fill(j, subsequent_indent='  ', width=72)
        return str