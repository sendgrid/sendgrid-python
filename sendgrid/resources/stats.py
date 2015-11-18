try:
    from urllib.parse import urlencode
except ImportError:  # Python 2
    from urllib import urlencode
    
class Stats(object):
    """Global Stats provide all of your user's email statistics for a given date range."""
    
    def __init__(self, client, **opts):
        """
        Constructs SendGrid Stats object.
        
        See https://sendgrid.com/docs/API_Reference/Web_API_v3/Stats/global.html
        """
        self._name = None
        self._base_endpoint = "/v3/stats?"
        self._endpoint = "/v3/stats?"
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
        
    # Gets email statistics.
    def get(self, start_date, end_date=None, aggregated_by=None):
        # Required
        args = {'start_date': start_date}
        # Optional arguements
        if end_date: 
            args['end_date'] = end_date
        if aggregated_by:
            args['aggregated_by'] = aggregated_by
        self._endpoint = self._base_endpoint + urlencode(args)
        return self.client.get(self)