class WhitelabelDomains(object):

    def __init__(self, client, **opts):
        """
        Constructs SendGrid WhitelabelDomains object.

        See https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/domains.html
        """
        self._base_endpoint = '/v3/whitelabel/domains'
        self._endpoint = '/v3/whitelabel/domains'
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
        Get a list of whitelabel domains
        """
        self.endpoint = self._base_endpoint
        return self.client.get(self)

    def post(self, domain, subdomain, username, default):
        """
        Create a new whitelabel domain

        :param domain: string
        :param subdomain: string
        :param username: string
        :param default: bool
        """
        data = {}
        data['domain'] = domain
        data['subdomain'] = subdomain
        data['username'] = username
        data['default'] = default

        self.endpoint = self._base_endpoint
        return self.client.post(self, data)

    def delete(self, id):
        """
        Delete a whitelabel domain

        :param id: int
        """
        self.endpoint = self._base_endpoint + '/' + str(id)
        return self.client.delete(self)

    def patch(self, id, default):
        """
        Update a whitelabel domain

        :param id: int
        :param default: bool
        """
        data = {}
        data['default'] = default

        self.endpoint = self._base_endpoint + '/' + str(id)
        return self.client.patch(self, data)
