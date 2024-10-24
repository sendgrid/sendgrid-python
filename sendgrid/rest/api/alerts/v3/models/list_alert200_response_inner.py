from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.alerts.v3.models.type1 import Type1



class ListAlert200ResponseInner:
    def __init__(
            self,
            created_at: Optional[int]=None,
            email_to: Optional[str]=None,
            id: Optional[int]=None,
            percentage: Optional[int]=None,
            type: Optional[Type1]=None,
            updated_at: Optional[int]=None,
            frequency: Optional[str]=None
    ):
        self.created_at=created_at
        self.email_to=email_to
        self.id=id
        self.percentage=percentage
        self.type=type
        self.updated_at=updated_at
        self.frequency=frequency

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "created_at": self.created_at,
            "email_to": self.email_to,
            "id": self.id,
            "percentage": self.percentage,
            "type": self.type,
            "updated_at": self.updated_at,
            "frequency": self.frequency
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListAlert200ResponseInner(
            created_at=payload.get('created_at'),
            email_to=payload.get('email_to'),
            id=payload.get('id'),
            percentage=payload.get('percentage'),
            type=payload.get('type'),
            updated_at=payload.get('updated_at'),
            frequency=payload.get('frequency')
        ) 

