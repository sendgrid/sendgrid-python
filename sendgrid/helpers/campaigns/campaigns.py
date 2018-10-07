class Campaigns(object):
    def __init__(self, limit=10, offset=0):
        self._limit = limit
        self._offset = offset

    def get(self, limit=None, offset=None):
        """Get all available campaigns

        Stores all Campaigns in 'campaigns' property and retrieves/populates
        campaign IDs, which are stored in 'ids' property.

        :param limit: Number of results to receive
        :type limit: int
        :param offset:  Index of first campaign to receive
        :type offset: int
        :return: List of Campaigns
        :rtype: list(Campaign)
        """
        params = {}
        if limit is None:
            limit = self._limit
        if isinstance(limit, int):
            params["limit"] = self._limit

        if offset is None:
            offset = self._offset
        if isinstance(offset, int):
            params["offset"] = offset

        return params

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = int(value)

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = int(value)
