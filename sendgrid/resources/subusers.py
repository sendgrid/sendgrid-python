class Subusers(object):

    def __init__(self, client, **opts):
        """
        Constructs SendGrid Subusers object.

        https://sendgrid.com/docs/API_Reference/Web_API_v3/subusers.html
        """
        self._base_endpoint = "/v3/subusers"
        self._endpoint = "/v3/subusers"
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
        Get a list of subusers
        """
        self.endpoint = self._base_endpoint
        return self.client.get(self)

    def post(self, username, email, password, ips = []):
        """
        Create a new subuser

        :param username: string
        :param email: string
        :param password: string
        :param ips: string[]
        """
        data = {}
        data['username'] = username
        data['email'] = email
        data['password'] = password
        data['ips'] = ips

        self.endpoint = self._base_endpoint
        return self.client.post(self, data)

    def delete(self, username):
        """
        Delete a subuser

        :param username: string
        """
        self.endpoint = self._base_endpoint + "/" + username
        return self.client.delete(self)

    def patch(self, username, disabled):
        """
        Enable/disable a subuser

        :param username: string
        :param disabled: bool
        """
        data = {}
        data['disabled'] = disabled

        self.endpoint = self._base_endpoint + "/" + username
        return self.client.patch(self, data)
