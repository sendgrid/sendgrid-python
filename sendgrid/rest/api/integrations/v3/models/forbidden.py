from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class Forbidden:
    def __init__(
            self,
            message: Optional[str]=None
    ):
        self.message=message

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "message": self.message
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return Forbidden(
            message=payload.get('message')
        ) 

