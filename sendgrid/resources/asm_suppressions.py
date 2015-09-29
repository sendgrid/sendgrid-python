class ASMSuppressions(object):
    """Advanced Suppression Manager gives your recipients more control over the types of emails they want to receive 
       by letting them opt out of messages from a certain type of email.
       
       Suppressions are email addresses that can be added to groups to prevent certain types of emails from being 
       delivered to those addresses.
       """
    
    def __init__(self, client, **opts):
        """
        Constructs SendGrid ASM suppressions object.
        
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
        
    # Get suppressed addresses for a given group id.
    def get(self, id=None, email=None):
        if id == None and email == None:
            return self.client.get(self)
        
        if isinstance(id, int):
            self._endpoint = self._base_endpoint + "/" + str(id) + "/suppressions"
            return self.client.get(self)
        
        if isinstance(email, str):
            self._endpoint = "/v3/asm/suppressions/" + email
            
        return self.client.get(self)
    
    # Add recipient addresses to the suppressions list for a given group.
    # If the group has been deleted, this request will add the address to the global suppression.
    def post(self, id, emails):
        self._endpoint = self._base_endpoint + "/" + str(id) + "/suppressions"
        data = {}
        data["recipient_emails"] = emails
        return self.client.post(self, data)

    # Delete a recipient email from the suppressions list for a group.
    def delete(self, id, email):
        self.endpoint = self._base_endpoint + "/" + str(id) + "/suppressions/" + email
        return self.client.delete(self)