from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.email_activity.v3.models.status import Status



class AbbvMessage:
    def __init__(
            self,
            from_email: Optional[str]=None,
            msg_id: Optional[str]=None,
            subject: Optional[str]=None,
            to_email: Optional[str]=None,
            status: Optional[Status]=None,
            opens_count: Optional[int]=None,
            clicks_count: Optional[int]=None,
            last_event_time: Optional[str]=None
    ):
        self.from_email=from_email
        self.msg_id=msg_id
        self.subject=subject
        self.to_email=to_email
        self.status=status
        self.opens_count=opens_count
        self.clicks_count=clicks_count
        self.last_event_time=last_event_time

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "from_email": self.from_email,
            "msg_id": self.msg_id,
            "subject": self.subject,
            "to_email": self.to_email,
            "status": self.status,
            "opens_count": self.opens_count,
            "clicks_count": self.clicks_count,
            "last_event_time": self.last_event_time
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AbbvMessage(
            from_email=payload.get('from_email'),
            msg_id=payload.get('msg_id'),
            subject=payload.get('subject'),
            to_email=payload.get('to_email'),
            status=payload.get('status'),
            opens_count=payload.get('opens_count'),
            clicks_count=payload.get('clicks_count'),
            last_event_time=payload.get('last_event_time')
        ) 

