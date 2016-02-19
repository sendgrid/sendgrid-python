import json
from .version import __version__
from socket import timeout
try:
    import urllib.request as urllib_request
    from urllib.parse import urlencode
    from urllib.error import HTTPError
except ImportError:  # Python 2
    import urllib2 as urllib_request
    from urllib2 import HTTPError
    from urllib import urlencode

from .exceptions import SendGridClientError, SendGridServerError
from .resources.api_keys import APIKeys
from .resources.asm_groups import ASMGroups
from .resources.asm_suppressions import ASMSuppressions
from .resources.asm_global_suppressions import ASMGlobalSuppressions
from .resources.suppressions import Suppressions
from .resources.stats import Stats
from .resources.subusers import Subusers
from .resources.whitelabel_domains import WhitelabelDomains
from .resources.whitelabel_ips import WhitelabelIPs
from .resources.ip_pools import IPPools
from .resources.ip_addresses import IPAddresses

class SendGridAPIClient(object):

    """SendGrid API."""

    def __init__(self, apikey, **opts):
        """
        Construct SendGrid API object.

        Args:
            apikey: SendGrid API key
            opts: You can pass in host or proxies
        """
        self._apikey = apikey
        self.useragent = 'sendgrid/' + __version__ + ';python_v3'
        self.host = opts.get('host', 'https://api.sendgrid.com')
        # urllib cannot connect to SSL servers using proxies
        self.proxies = opts.get('proxies', None)
        self._basic = opts.get('basic', False)
        self.timeout = opts.get('timeout', 10)

        self.apikeys = APIKeys(self)
        self.asm_groups = ASMGroups(self)
        self.asm_suppressions = ASMSuppressions(self)
        self.asm_global_suppressions = ASMGlobalSuppressions(self)
        self.suppressions = Suppressions(self)
        self.stats = Stats(self)
        self.subusers = Subusers(self)
        self.whitelabel_domains = WhitelabelDomains(self)
        self.whitelabel_ips = WhitelabelIPs(self)
        self.ip_pools = IPPools(self)
        self.ips = IPAddresses(self)

    @property
    def apikey(self):
        return self._apikey

    @apikey.setter
    def apikey(self, value):
        self._apikey = value

    def _build_request(self, url, json_header=False, method='GET', data=None):
        if self.proxies:
            proxy_support = urllib_request.ProxyHandler(self.proxies)
            opener = urllib_request.build_opener(proxy_support)
            urllib_request.install_opener(opener)
        req = urllib_request.Request(url)
        req.get_method = lambda: method
        req.add_header('User-Agent', self.useragent)
        req.add_header('Authorization', ('Basic ' if self._basic else 'Bearer ') + self.apikey)
        if json_header:
            req.add_header('Content-Type', 'application/json')
        try:
            if data:
                response = urllib_request.urlopen(req, json.dumps(data))
            else:
                response = urllib_request.urlopen(req, timeout=self.timeout)
        except HTTPError as e:
            if 400 <= e.code < 500:
                raise SendGridClientError(e.code, e.read())
            elif 500 <= e.code < 600:
                raise SendGridServerError(e.code, e.read())
            else:
                assert False
        except timeout as e:
            raise SendGridClientError(408, 'Request timeout')
        body = response.read()
        return response.getcode(), body

    def get(self, api):
        url = self.host + api.endpoint
        response, body = self._build_request(url, False, 'GET')
        return response, body

    def post(self, api, data):
        url = self.host + api.endpoint
        response, body = self._build_request(url, True, 'POST', data)
        return response, body

    def delete(self, api):
        url = self.host + api.endpoint
        response, body = self._build_request(url, False, 'DELETE')
        return response, body

    def patch(self, api, data):
        url = self.host + api.endpoint
        response, body = self._build_request(url, True, 'PATCH', data)
        return response, body
