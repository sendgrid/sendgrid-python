class WhitelabelIPs(object):

    def __init__(self, client, **opts):
        """
        Constructs SendGrid WhitelabelIPs object.

        See https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/ips.html
        """
        self._base_endpoint = '/v3/whitelabel/ips'
        self._endpoint = '/v3/whitelabel/ips'
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
        Get a list of whitelabel IPs
        """
        self.endpoint = self._base_endpoint
        return self.client.get(self)

    def post(self, ip, domain, subdomain):
        """
        Create a new whitelabel IP

        :param ip: string
        :param domain: string
        :param subdomain: string
        """
        data = {}
        data['ip'] = ip
        data['domain'] = domain
        data['subdomain'] = subdomain

        self.endpoint = self._base_endpoint
        return self.client.post(self, data)

    def delete(self, id):
        """
        Delete a whitelabel IP

        :param id: int
        """
        self.endpoint = self._base_endpoint + '/' + str(id)
        return self.client.delete(self)
