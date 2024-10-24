from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ContactsError:
    def __init__(
            self,
            message: Optional[str]=None,
            field: Optional[str]=None,
            error_id: Optional[str]=None,
            parameter: Optional[str]=None
    ):
        self.message=message
        self.field=field
        self.error_id=error_id
        self.parameter=parameter

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "message": self.message,
            "field": self.field,
            "error_id": self.error_id,
            "parameter": self.parameter
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactsError(
            message=payload.get('message'),
            field=payload.get('field'),
            error_id=payload.get('error_id'),
            parameter=payload.get('parameter')
        ) 
