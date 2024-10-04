from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.email_activity.v3.models.bounce_type import BounceType
from sendgrid.rest.api.email_activity.v3.models.event_name import EventName


class Event:
    def __init__(
        self,
        event_name: Optional[EventName] = None,
        processed: Optional[str] = None,
        reason: Optional[str] = None,
        attempt_num: Optional[int] = None,
        url: Optional[str] = None,
        bounce_type: Optional[BounceType] = None,
        http_user_agent: Optional[str] = None,
        mx_server: Optional[str] = None,
    ):
        self.event_name = event_name
        self.processed = processed
        self.reason = reason
        self.attempt_num = attempt_num
        self.url = url
        self.bounce_type = bounce_type
        self.http_user_agent = http_user_agent
        self.mx_server = mx_server

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "event_name": self.event_name,
                "processed": self.processed,
                "reason": self.reason,
                "attempt_num": self.attempt_num,
                "url": self.url,
                "bounce_type": self.bounce_type,
                "http_user_agent": self.http_user_agent,
                "mx_server": self.mx_server,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return Event(
            event_name=payload.get("event_name"),
            processed=payload.get("processed"),
            reason=payload.get("reason"),
            attempt_num=payload.get("attempt_num"),
            url=payload.get("url"),
            bounce_type=payload.get("bounce_type"),
            http_user_agent=payload.get("http_user_agent"),
            mx_server=payload.get("mx_server"),
        )
