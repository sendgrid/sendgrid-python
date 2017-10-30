class SpamCheck(object):

    def __init__(self, enable=None, threshold=None, post_to_url=None):
        self._enable = None
        self._threshold = None
        self._post_to_url = None

        if enable is not None:
            self.enable = enable

        if threshold is not None:
            self.threshold = threshold

        if post_to_url is not None:
            self.post_to_url = post_to_url

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        self._threshold = value

    @property
    def post_to_url(self):
        return self._post_to_url

    @post_to_url.setter
    def post_to_url(self, value):
        self._post_to_url = value

    def get(self):
        spam_check = {}
        if self.enable is not None:
            spam_check["enable"] = self.enable

        if self.threshold is not None:
            spam_check["threshold"] = self.threshold

        if self.post_to_url is not None:
            spam_check["post_to_url"] = self.post_to_url
        return spam_check
