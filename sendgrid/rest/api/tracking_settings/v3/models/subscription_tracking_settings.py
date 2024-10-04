from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class SubscriptionTrackingSettings:
    def __init__(
        self,
        enabled: Optional[bool] = None,
        html_content: Optional[str] = None,
        landing: Optional[str] = None,
        plain_content: Optional[str] = None,
        replace: Optional[str] = None,
        url: Optional[str] = None,
    ):
        self.enabled = enabled
        self.html_content = html_content
        self.landing = landing
        self.plain_content = plain_content
        self.replace = replace
        self.url = url

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "enabled": self.enabled,
                "html_content": self.html_content,
                "landing": self.landing,
                "plain_content": self.plain_content,
                "replace": self.replace,
                "url": self.url,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SubscriptionTrackingSettings(
            enabled=payload.get("enabled"),
            html_content=payload.get("html_content"),
            landing=payload.get("landing"),
            plain_content=payload.get("plain_content"),
            replace=payload.get("replace"),
            url=payload.get("url"),
        )
