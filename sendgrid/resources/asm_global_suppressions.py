class ASMGlobalSuppressions(object):
    """Advanced Suppression Manager (ASM) gives your recipients more control over the types of emails they want to receive 
       by letting them opt out of messages from a certain type of email.
       
       Global Suppressions are email addresses that will not receive any emails.
       """
    
    def __init__(self, client, **opts):
        """
        Constructs SendGrid ASM suppressions object.
        
        See https://sendgrid.com/docs/API_Reference/Web_API_v3/Advanced_Suppression_Manager/index.html and
        https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/global_suppressions.html
        """
        self._name = None
        self._base_endpoint = "/v3/asm/suppressions/global"
        self._endpoint = "/v3/asm/suppressions/global"
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
        
    # Determine if an email belongs to the global suppression group
    def get(self, email):
        self._endpoint = self._base_endpoint + '/' + email
        return self.client.get(self)
        
    # Add an email to the global suppressions group
    def post(self, emails):
        self._endpoint = self._base_endpoint
        data = {}
        data["recipient_emails"] = emails
        return self.client.post(self, data)
        
    # Remove an email from the global suppressions group
    def delete(self, email):
        self._endpoint = self._base_endpoint + '/' + email
        return self.client.delete(self)