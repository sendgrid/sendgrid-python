class Campaign(object):
    """Campaign class object for campaign API queries

    Required parameter:
        title: str

    Optional parameters:
        categories: list(str)
        custom_unsubscribe_url: str
        editor: str ['code' | 'design']
        html_content: str
        ip_pool: str
        list_ids: list(int)
        plain_content: str
        segment_ids: list(int)
        sender_id: int
        subject: str
        suppression_group_id: int

    :param kwargs: List of inputs
    """
    def __init__(self, **kwargs):
        self._categories = []
        self._custom_unsubscribe_url = None
        self._editor = None
        self._html_content = None
        self._id = None
        self._ip_pool = None
        self._list_ids = []
        self._plain_content = None
        self._segment_ids = []
        self._sender_id = None
        self._status = ""
        self._subject = None
        self._suppression_group_id = None
        self._title = ""

        for key, val in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, val)

    def copy(self, new_title):
        """Creates a copy of the campaign

        :param new_title: Title of new campaign
        :type new_title: str
        :return: Campaign
        """
        new_camp = Campaign(**self.get())
        new_camp.title = new_title
        return new_camp

    def get(self):
        """Returns dict suitable for queries"""
        body = {"title": self.title}
        if self.categories:
            body["categories"] = [str(i) for i in self.categories]
        if self.custom_unsubscribe_url is not None:
            body["custom_unsubscribe_url"] = self.custom_unsubscribe_url
        if self.editor is not None:
            body["editor"] = self.editor
        if self.html_content is not None:
            body["html_content"] = self.html_content
        if self.ip_pool is not None:
            body["ip_pool"] = self.ip_pool
        if self.list_ids and all(isinstance(i, int) for i in self.list_ids):
            body["list_ids"] = self.list_ids
        if self.plain_content:
            body["plain_content"] = self.plain_content
        if self.segment_ids\
                and all(isinstance(i, int) for i in self.segment_ids):
            body["segment_ids"] = self.segment_ids
        if self.sender_id is not None:
            body["sender_id"] = self.sender_id
        if self.subject is not None:
            body["subject"] = self.subject
        if self.suppression_group_id is not None:
            body["suppression_group_id"] = self.suppression_group_id
        return body

    def get_patch(self):
        return {
            "title": self.title,
            "subject": self.subject,
            "categories": self.categories,
            "html_content": self.html_content,
            "plain_content": self.plain_content
        }

    def patch(self, **kwargs):
        """Updates the campaign with

        Optional inputs:
            title: str
            subject: str
            categories: list(str)
            html_content: str
            plain_content: str

        :param kwargs: Dictionary of optional inputs
        :type kwargs: dict
        :return: Updated get() dict
        """
        if "title" in kwargs:
            self.title = kwargs["title"]
        if "subject" in kwargs:
            self.subject = kwargs["subject"]
        if "categories" in kwargs:
            self.categories = kwargs["categories"]
        if "html_content" in kwargs:
            self.html_content = kwargs["html_content"]
        if "plain_content" in kwargs:
            self.plain_content = kwargs["plain_content"]
        return self.get_patch()

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        self._categories = value

    @property
    def custom_unsubscribe_url(self):
        return self._custom_unsubscribe_url

    @custom_unsubscribe_url.setter
    def custom_unsubscribe_url(self, value):
        self._custom_unsubscribe_url = value

    @property
    def editor(self):
        return self._editor

    @editor.setter
    def editor(self, value):
        value = str(value).lower()
        if value in ["code", "design"]:
            self._editor = value

    @property
    def html_content(self):
        return self._html_content

    @html_content.setter
    def html_content(self, value):
        self._html_content = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def ip_pool(self):
        return self._ip_pool

    @ip_pool.setter
    def ip_pool(self, value):
        self._ip_pool = value

    @property
    def list_ids(self):
        return self._list_ids

    @list_ids.setter
    def list_ids(self, value):
        self._list_ids = value

    @property
    def plain_content(self):
        return self._plain_content

    @plain_content.setter
    def plain_content(self, value):
        self._plain_content = value

    @property
    def segment_ids(self):
        return self._segment_ids

    @segment_ids.setter
    def segment_ids(self, value):
        self._segment_ids = value

    @property
    def sender_id(self):
        return self._sender_id

    @sender_id.setter
    def sender_id(self, value):
        self._sender_id = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        if isinstance(value, str) or isinstance(value, type(None)):
            self._subject = value

    @property
    def suppression_group_id(self):
        return self._suppression_group_id

    @suppression_group_id.setter
    def suppression_group_id(self, value):
        self._suppression_group_id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value:
            self._title = str(value)
