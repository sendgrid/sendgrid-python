import urllib

class IPAddresses(object):

    def __init__(self, client, **opts):
        """
        Constructs SendGrid IP Pools object.

        See https://sendgrid.com/docs/API_Reference/Web_API_v3/IP_Management/ip_addresses.html
        """
        self._base_endpoint = '/v3/ips'
        self._endpoint = '/v3/ips'
        self._client = client

    @property
    def base_endpoint(self):
        return self._base_endpoint

    @property
    def endpoint(self):
        endpoint = self._endpoint
        return endpoint

    @endpoint.setter
    def endpoint(self, value):
        self._endpoint = value

    @property
    def client(self):
        return self._client

    def get(self):
        """
        List all IP addresses
        """
        self.endpoint = self._base_endpoint
        return self.client.get(self)

    def post(self, ip_pool, ip):
        """
        Add an IP address to the specified IP Pool

        :param ip_pool: str
        :param ip: str
        """
        data = {}
        data['ip'] = ip

        self.endpoint = self._base_endpoint + '/pools/' + urllib.quote_plus(ip_pool) + '/ips'
        return self.client.post(self, data)

    def delete(self, ip_pool, ip):
        """
        Delete an IP address from the specified IP Pool

        :param ip_pool: str
        :param ip: str
        """
        self.endpoint = (
            self._base_endpoint +
            '/pools/' + urllib.quote_plus(ip_pool) +
            '/ips/' + urllib.quote_plus(ip))
        return self.client.delete(self)
