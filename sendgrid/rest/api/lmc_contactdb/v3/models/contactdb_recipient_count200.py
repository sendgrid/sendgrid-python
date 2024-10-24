from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ContactdbRecipientCount200:
    def __init__(
            self,
            recipient_count: Optional[float]=None
    ):
        self.recipient_count=recipient_count

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "recipient_count": self.recipient_count
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactdbRecipientCount200(
            recipient_count=payload.get('recipient_count')
        ) 

