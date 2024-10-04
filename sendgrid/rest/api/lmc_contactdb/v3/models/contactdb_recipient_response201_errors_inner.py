from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ContactdbRecipientResponse201ErrorsInner:
    def __init__(
            self,
            message: Optional[str]=None,
            error_indices: Optional[List[float]]=None
    ):
        self.message=message
        self.error_indices=error_indices

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "message": self.message,
            "error_indices": self.error_indices
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactdbRecipientResponse201ErrorsInner(
            message=payload.get('message'),
            error_indices=payload.get('error_indices')
        ) 

