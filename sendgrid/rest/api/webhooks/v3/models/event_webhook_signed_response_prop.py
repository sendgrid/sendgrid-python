from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class EventWebhookSignedResponseProp:
    def __init__(
            self,
            public_key: Optional[str]=None
    ):
        self.public_key=public_key

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "public_key": self.public_key
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return EventWebhookSignedResponseProp(
            public_key=payload.get('public_key')
        ) 

