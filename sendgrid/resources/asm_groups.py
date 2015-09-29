class ASMGroups(object):
    """Advanced Suppression Manager gives your recipients more control over the types of emails they want to receive 
       by letting them opt out of messages from a certain type of email.
       
       Groups are specific types of email you would like your recipients to be able to unsubscribe from or subscribe to. 
       For example: Daily Newsletters, Invoices, System Alerts.
       """
    
    def __init__(self, client, **opts):
        """
        Constructs SendGrid ASM group object.
        
        See https://sendgrid.com/docs/API_Reference/Web_API_v3/Advanced_Suppression_Manager/index.html and
        https://sendgrid.com/docs/API_Reference/Web_API_v3/Advanced_Suppression_Manager/groups.html
        """
        self._name = None
        self._base_endpoint = "/v3/asm/groups"
        self._endpoint = "/v3/asm/groups"
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
        
    # Retrieve all suppression groups associated with the user.
    def get(self, id=None):
        if id == None:
            return self.client.get(self)
        
        if isinstance(id, int):
            self._endpoint = self._base_endpoint + "/" + str(id)
            return self.client.get(self)
        
        if len(id) > 1:
            count = 0
            for i in id:
                if count == 0:
                    self._endpoint = self._endpoint + "?id=" + str(i)
                else:
                    self._endpoint = self._endpoint + "&id=" + str(i)
                count = count + 1
            
        return self.client.get(self)