from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class EventWebhookNoDatesResponse:
    def __init__(
        self,
        enabled: Optional[bool] = None,
        url: Optional[str] = None,
        account_status_change: Optional[bool] = None,
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
        id: Optional[str] = None,
        oauth_client_id: Optional[str] = None,
        oauth_token_url: Optional[str] = None,
        public_key: Optional[str] = None,
    ):
        self.enabled = enabled
        self.url = url
        self.account_status_change = account_status_change
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
        self.id = id
        self.oauth_client_id = oauth_client_id
        self.oauth_token_url = oauth_token_url
        self.public_key = public_key

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "enabled": self.enabled,
                "url": self.url,
                "account_status_change": self.account_status_change,
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
                "id": self.id,
                "oauth_client_id": self.oauth_client_id,
                "oauth_token_url": self.oauth_token_url,
                "public_key": self.public_key,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return EventWebhookNoDatesResponse(
            enabled=payload.get("enabled"),
            url=payload.get("url"),
            account_status_change=payload.get("account_status_change"),
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
            id=payload.get("id"),
            oauth_client_id=payload.get("oauth_client_id"),
            oauth_token_url=payload.get("oauth_token_url"),
            public_key=payload.get("public_key"),
        )
