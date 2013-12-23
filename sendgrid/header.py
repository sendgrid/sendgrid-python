try:
    import json
except ImportError:
    import simplejson as json


class SMTPAPIHeader(object):
    def __init__(self):
        self.data = {}

    def add_substitution(self, key, val):
        if 'sub' not in self.data:
            self.data['sub'] = {}
        self.data[key].append(val)

    def set_substitution(self, key, val):
        if 'sub' not in self.data:
            self.data['sub'] = {}
        if type(val) is str:
            self.data[key] = [val]
        elif type(val) is list:
            self.data[key] = val

    def add_unique_args(self, key, val):
        if 'unique_args' not in self.data:
            self.data['unique_args'] = {}
        self.data['unique_args'][key] = val

    def set_unique_args(self, val):
        if type(val) is dict:
            self.data['unique_args'] = val

    def add_category(self, category):
        if 'category' not in self.data:
            self.data['category'] = []
        self.data['category'].append(category)

    def set_category(self, category):
        self.data['category'] = category

    def add_section(self, key, section):
        if 'section' not in self.data:
            self.data['section'] = {}
        self.data['section'][key] = section

    def set_section(self, val):
        self.data['section'] = val

    def add_filter(self, fltr, setting, val):
        if 'filters' not in self.data:
            self.data['filters'] = {}
        if fltr not in self.data['filters']:
            self.data['filters'][fltr] = {}
        if 'settings' not in self.data['filters'][fltr]:
            self.data['filters'][fltr]['settings'] = {}
        self.data['filters'][fltr]['settings'][setting] = val

    def api_header_as_json(self):
        return json.dumps(self.data)

