class APIKeys(object):
    """The API Keys feature allows customers to be able to generate an API Key credential 
    which can be used for authentication with the SendGrid v3 Web API or the Mail API Endpoint"""
    
    def __init__(self, client, **opts):
        """
        Constructs SendGrid APIKeys object.
        
        See https://sendgrid.com/docs/API_Reference/Web_API_v3/API_Keys/index.html
        """
        self._name = None
        self._base_endpoint = "/v3/api_keys"
        self._endpoint = "/v3/api_keys"
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
        
    # Create a new API key with name (string)
    def post(self, name):
        data = {}
        self.name = name
        data['name'] = self.name
        return self.client.post(self, data)
        
    # Delete a API key
    def delete(self, api_key_id):
        self.endpoint = self._base_endpoint + "/" + api_key_id
        return self.client.delete(self)
        
    # Update a API key's name
    def patch(self, api_key_id, name):
        data = {}
        self.name = name
        data['name'] = self.name
        self.endpoint = self._base_endpoint + "/" + api_key_id
        return self.client.patch(self, data)