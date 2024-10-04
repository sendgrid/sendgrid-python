from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mail.v3.models.send_mail_request_tracking_settings_click_tracking import SendMailRequestTrackingSettingsClickTracking
from sendgrid.rest.api.mail.v3.models.send_mail_request_tracking_settings_ganalytics import SendMailRequestTrackingSettingsGanalytics
from sendgrid.rest.api.mail.v3.models.send_mail_request_tracking_settings_open_tracking import SendMailRequestTrackingSettingsOpenTracking
from sendgrid.rest.api.mail.v3.models.send_mail_request_tracking_settings_subscription_tracking import SendMailRequestTrackingSettingsSubscriptionTracking



class SendMailRequestTrackingSettings:
    def __init__(
            self,
            click_tracking: Optional[SendMailRequestTrackingSettingsClickTracking]=None,
            open_tracking: Optional[SendMailRequestTrackingSettingsOpenTracking]=None,
            subscription_tracking: Optional[SendMailRequestTrackingSettingsSubscriptionTracking]=None,
            ganalytics: Optional[SendMailRequestTrackingSettingsGanalytics]=None
    ):
        self.click_tracking=click_tracking
        self.open_tracking=open_tracking
        self.subscription_tracking=subscription_tracking
        self.ganalytics=ganalytics

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "click_tracking": self.click_tracking,
            "open_tracking": self.open_tracking,
            "subscription_tracking": self.subscription_tracking,
            "ganalytics": self.ganalytics
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendMailRequestTrackingSettings(
            click_tracking=payload.get('click_tracking'),
            open_tracking=payload.get('open_tracking'),
            subscription_tracking=payload.get('subscription_tracking'),
            ganalytics=payload.get('ganalytics')
        ) 

