class Subusers(object):

    def __init__(self, client, **opts):
        """
        Constructs SendGrid Subusers object.

        See https://sendgrid.com/docs/API_Reference/Web_API_v3/subusers.html
        """
        self._name = None
        self._base_endpoint = "/v3/subusers"
        self._endpoint = "/v3/subusers"
        self._client = client

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

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

    # Get a list of active API keys
    def get(self):
        return self.client.get(self)

    # Create a new subuser with username, email, password (string) and IP list (string[])
    def post(self, username, email, password, ips = []):
        data = {}
        self.username = username
        self.email = email
        self.password = password
        data['username'] = self.username
        data['email'] = self.email
        data['password'] = self.password
        data['ips'] = ips
        return self.client.post(self, data)

    # Delete a subuser
    def delete(self, username):
        self.endpoint = self._base_endpoint + "/" + username
        return self.client.delete(self)

    # Enable/disable a subuser
    def patch(self, username, disabled):
        data = {}
        self.disabled = disabled
        data['disabled'] = self.disabled
        self.endpoint = self._base_endpoint + "/" + username
        return self.client.patch(self, data)
