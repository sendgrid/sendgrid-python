from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class EventWebhookRequest:
    def __init__(
        self,
        enabled: Optional[bool] = None,
        url: Optional[str] = None,
        group_resubscribe: Optional[bool] = None,
        delivered: Optional[bool] = None,
        group_unsubscribe: Optional[bool] = None,
        spam_report: Optional[bool] = None,
        bounce: Optional[bool] = None,
        deferred: Optional[bool] = None,
        unsubscribe: Optional[bool] = None,
        processed: Optional[bool] = None,
        open: Optional[bool] = None,
        click: Optional[bool] = None,
        dropped: Optional[bool] = None,
        friendly_name: Optional[str] = None,
        oauth_client_id: Optional[str] = None,
        oauth_client_secret: Optional[str] = None,
        oauth_token_url: Optional[str] = None,
    ):
        self.enabled = enabled
        self.url = url
        self.group_resubscribe = group_resubscribe
        self.delivered = delivered
        self.group_unsubscribe = group_unsubscribe
        self.spam_report = spam_report
        self.bounce = bounce
        self.deferred = deferred
        self.unsubscribe = unsubscribe
        self.processed = processed
        self.open = open
        self.click = click
        self.dropped = dropped
        self.friendly_name = friendly_name
        self.oauth_client_id = oauth_client_id
        self.oauth_client_secret = oauth_client_secret
        self.oauth_token_url = oauth_token_url

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "enabled": self.enabled,
                "url": self.url,
                "group_resubscribe": self.group_resubscribe,
                "delivered": self.delivered,
                "group_unsubscribe": self.group_unsubscribe,
                "spam_report": self.spam_report,
                "bounce": self.bounce,
                "deferred": self.deferred,
                "unsubscribe": self.unsubscribe,
                "processed": self.processed,
                "open": self.open,
                "click": self.click,
                "dropped": self.dropped,
                "friendly_name": self.friendly_name,
                "oauth_client_id": self.oauth_client_id,
                "oauth_client_secret": self.oauth_client_secret,
                "oauth_token_url": self.oauth_token_url,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return EventWebhookRequest(
            enabled=payload.get("enabled"),
            url=payload.get("url"),
            group_resubscribe=payload.get("group_resubscribe"),
            delivered=payload.get("delivered"),
            group_unsubscribe=payload.get("group_unsubscribe"),
            spam_report=payload.get("spam_report"),
            bounce=payload.get("bounce"),
            deferred=payload.get("deferred"),
            unsubscribe=payload.get("unsubscribe"),
            processed=payload.get("processed"),
            open=payload.get("open"),
            click=payload.get("click"),
            dropped=payload.get("dropped"),
            friendly_name=payload.get("friendly_name"),
            oauth_client_id=payload.get("oauth_client_id"),
            oauth_client_secret=payload.get("oauth_client_secret"),
            oauth_token_url=payload.get("oauth_token_url"),
        )
