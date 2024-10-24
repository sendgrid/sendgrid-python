from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ListRecipientsResponse:
    def __init__(
            self,
            recipients: Optional[List[object]]=None
    ):
        self.recipients=recipients

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "recipients": self.recipients
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListRecipientsResponse(
            recipients=payload.get('recipients')
        ) 

