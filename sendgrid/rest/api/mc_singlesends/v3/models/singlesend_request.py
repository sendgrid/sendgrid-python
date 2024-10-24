from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_singlesends.v3.models.singlesend_request_email_config import SinglesendRequestEmailConfig
from sendgrid.rest.api.mc_singlesends.v3.models.singlesend_request_send_to import SinglesendRequestSendTo



class SinglesendRequest:
    def __init__(
            self,
            name: Optional[str]=None,
            categories: Optional[List[str]]=None,
            send_at: Optional[datetime]=None,
            send_to: Optional[SinglesendRequestSendTo]=None,
            email_config: Optional[SinglesendRequestEmailConfig]=None
    ):
        self.name=name
        self.categories=categories
        self.send_at=send_at
        self.send_to=send_to
        self.email_config=email_config

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "name": self.name,
            "categories": self.categories,
            "send_at": self.send_at,
            "send_to": self.send_to,
            "email_config": self.email_config
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SinglesendRequest(
            name=payload.get('name'),
            categories=payload.get('categories'),
            send_at=payload.get('send_at'),
            send_to=payload.get('send_to'),
            email_config=payload.get('email_config')
        ) 

