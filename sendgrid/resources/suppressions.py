class Suppressions(object):
    
    def __init__(self, client, **opts):
        """
        Constructs SendGrid Suppressions object
        """
        self._name = None
        self._base_endpoint = "/v3/suppression/unsubscribes"
        self._endpoint = "/v3/suppression/unsubscribes"
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
        
    # Get all global suppressions
    def get(self):        
        return self.client.get(self)