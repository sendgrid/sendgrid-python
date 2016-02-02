import urllib

class IPPools(object):

    def __init__(self, client, **opts):
        """
        Constructs SendGrid IP Pools object.

        See https://sendgrid.com/docs/API_Reference/Web_API_v3/IP_Management/ip_pools.html
        """
        self._base_endpoint = '/v3/ips/pools'
        self._endpoint = '/v3/ips/pools'
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
        List all IP pools
        """
        self.endpoint = self._base_endpoint
        return self.client.get(self)

    def post(self, name):
        """
        Create a new IP pool

        :param name: str
        """
        data = {}
        data['name'] = name

        self.endpoint = self._base_endpoint
        return self.client.post(self, data)

    def delete(self, name):
        """
        Delete an IP pool

        :param name: str
        """
        self.endpoint = self._base_endpoint + '/' + urllib.quote_plus(name)
        return self.client.delete(self)
