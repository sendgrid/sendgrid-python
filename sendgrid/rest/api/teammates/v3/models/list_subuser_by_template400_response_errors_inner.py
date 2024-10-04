from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ListSubuserByTemplate400ResponseErrorsInner:
    def __init__(
            self,
            message: Optional[str]=None,
            field: Optional[str]=None
    ):
        self.message=message
        self.field=field

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "message": self.message,
            "field": self.field
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListSubuserByTemplate400ResponseErrorsInner(
            message=payload.get('message'),
            field=payload.get('field')
        ) 

