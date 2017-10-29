class Ganalytics(object):
    """Allows you to enable tracking provided by Google Analytics."""

    def __init__(self,
                 enable=None,
                 utm_source=None,
                 utm_medium=None,
                 utm_term=None,
                 utm_content=None,
                 utm_campaign=None):
        """Create a GAnalytics to enable, customize Google Analytics tracking.

        :param enable: If this setting is enabled.
        :type enable: boolean, optional
        :param utm_source: Name of the referrer source.
        :type utm_source: string, optional
        :param utm_medium: Name of the marketing medium (e.g. "Email").
        :type utm_medium: string, optional
        :param utm_term: Used to identify paid keywords.
        :type utm_term: string, optional
        :param utm_content: Used to differentiate your campaign from ads.
        :type utm_content: string, optional
        :param utm_campaign: The name of the campaign.
        :type utm_campaign: string, optional
        """
        self._enable = None
        self._utm_source = None
        self._utm_medium = None
        self._utm_term = None
        self._utm_content = None
        self._utm_campaign = None

        if enable is not None:
            self.enable = enable
        if utm_source is not None:
            self.utm_source = utm_source
        if utm_medium is not None:
            self.utm_medium = utm_medium
        if utm_term is not None:
            self.utm_term = utm_term
        if utm_content is not None:
            self.utm_content = utm_content
        if utm_campaign is not None:
            self.utm_campaign = utm_campaign

    @property
    def enable(self):
        """Indicates if this setting is enabled.

        :rtype: boolean
        """
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    @property
    def utm_source(self):
        """Name of the referrer source.

        e.g. Google, SomeDomain.com, or Marketing Email
        :rtype: string
        """
        return self._utm_source

    @utm_source.setter
    def utm_source(self, value):
        self._utm_source = value

    @property
    def utm_medium(self):
        """Name of the marketing medium (e.g. Email).

        :rtype: string
        """
        return self._utm_medium

    @utm_medium.setter
    def utm_medium(self, value):
        self._utm_medium = value

    @property
    def utm_term(self):
        """Used to identify any paid keywords.

        :rtype: string
        """
        return self._utm_term

    @utm_term.setter
    def utm_term(self, value):
        self._utm_term = value

    @property
    def utm_content(self):
        """Used to differentiate your campaign from advertisements.

        :rtype: string
        """
        return self._utm_content

    @utm_content.setter
    def utm_content(self, value):
        self._utm_content = value

    @property
    def utm_campaign(self):
        """The name of the campaign.

        :rtype: string
        """
        return self._utm_campaign

    @utm_campaign.setter
    def utm_campaign(self, value):
        self._utm_campaign = value

    def get(self):
        """
        Get a JSON-ready representation of this Ganalytics.

        :returns: This Ganalytics, ready for use in a request body.
        :rtype: dict
        """
        ganalytics = {}
        if self.enable is not None:
            ganalytics["enable"] = self.enable
        if self.utm_source is not None:
            ganalytics["utm_source"] = self.utm_source
        if self.utm_medium is not None:
            ganalytics["utm_medium"] = self.utm_medium
        if self.utm_term is not None:
            ganalytics["utm_term"] = self.utm_term
        if self.utm_content is not None:
            ganalytics["utm_content"] = self.utm_content
        if self.utm_campaign is not None:
            ganalytics["utm_campaign"] = self.utm_campaign
        return ganalytics


class TrackingSettings(object):
    """Settings to track how recipients interact with your email."""
    def __init__(self):
        """Create an empty TrackingSettings."""
        self._click_tracking = None
        self._open_tracking = None
        self._subscription_tracking = None
        self._ganalytics = None

    @property
    def click_tracking(self):
        """Allows you to track whether a recipient clicked a link in your email.

        :rtype: ClickTracking
        """
        return self._click_tracking

    @click_tracking.setter
    def click_tracking(self, value):
        self._click_tracking = value

    @property
    def open_tracking(self):
        """Allows you to track whether a recipient opened your email.

        :rtype: OpenTracking
        """
        return self._open_tracking

    @open_tracking.setter
    def open_tracking(self, value):
        self._open_tracking = value

    @property
    def subscription_tracking(self):
        """Settings for the subscription management link.

        :rtype: SubscriptionTracking
        """
        return self._subscription_tracking

    @subscription_tracking.setter
    def subscription_tracking(self, value):
        self._subscription_tracking = value

    @property
    def ganalytics(self):
        """Settings for Google Analytics.

        :rtype: Ganalytics
        """
        return self._ganalytics

    @ganalytics.setter
    def ganalytics(self, value):
        self._ganalytics = value

    def get(self):
        """
        Get a JSON-ready representation of this TrackingSettings.

        :returns: This TrackingSettings, ready for use in a request body.
        :rtype: dict
        """
        tracking_settings = {}
        if self.click_tracking is not None:
            tracking_settings["click_tracking"] = self.click_tracking.get()
        if self.open_tracking is not None:
            tracking_settings["open_tracking"] = self.open_tracking.get()
        if self.subscription_tracking is not None:
            tracking_settings[
                "subscription_tracking"] = self.subscription_tracking.get()
        if self.ganalytics is not None:
            tracking_settings["ganalytics"] = self.ganalytics.get()
        return
