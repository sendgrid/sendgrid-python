from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class EventWebhookDateResponseProps:
    def __init__(
            self,
            created_date: Optional[datetime]=None,
            updated_date: Optional[datetime]=None
    ):
        self.created_date=created_date
        self.updated_date=updated_date

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "created_date": self.created_date,
            "updated_date": self.updated_date
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return EventWebhookDateResponseProps(
            created_date=payload.get('created_date'),
            updated_date=payload.get('updated_date')
        ) 

