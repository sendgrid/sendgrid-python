from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.email_activity.v3.models.status3 import Status3



class EmailActivityResponseBaseProps:
    def __init__(
            self,
            from_email: Optional[str]=None,
            msg_id: Optional[str]=None,
            subject: Optional[str]=None,
            to_email: Optional[str]=None,
            status: Optional[Status3]=None
    ):
        self.from_email=from_email
        self.msg_id=msg_id
        self.subject=subject
        self.to_email=to_email
        self.status=status

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "from_email": self.from_email,
            "msg_id": self.msg_id,
            "subject": self.subject,
            "to_email": self.to_email,
            "status": self.status
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return EmailActivityResponseBaseProps(
            from_email=payload.get('from_email'),
            msg_id=payload.get('msg_id'),
            subject=payload.get('subject'),
            to_email=payload.get('to_email'),
            status=payload.get('status')
        ) 

