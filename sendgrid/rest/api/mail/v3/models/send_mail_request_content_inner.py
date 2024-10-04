from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SendMailRequestContentInner:
    def __init__(
            self,
            type: Optional[str]=None,
            value: Optional[str]=None
    ):
        self.type=type
        self.value=value

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "type": self.type,
            "value": self.value
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendMailRequestContentInner(
            type=payload.get('type'),
            value=payload.get('value')
        ) 

