class UtmTerm(object):
    """The UtmTerm of an Ganalytics."""

    def __init__(self, utm_term=None):
        """Create a UtmTerm object

        :param utm_term: Used to identify any paid keywords.

        :type utm_term: string, optional
        """
        self._utm_term = None
        
        if utm_term is not None:
            self.utm_term = utm_term

    @property
    def utm_term(self):
        """Used to identify any paid keywords.

        :rtype: string
        """
        return self._utm_term

    @utm_term.setter
    def utm_term(self, value):
        self._utm_term = value

    def get(self):
        """
        Get a JSON-ready representation of this UtmTerm.

        :returns: This UtmTerm, ready for use in a request body.
        :rtype: string
        """
        return self.utm_term