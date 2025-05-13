from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SuppressionGroup:
    def __init__(
            self,
            id: Optional[float]=None,
            name: Optional[str]=None,
            description: Optional[str]=None,
            is_default: Optional[bool]=None,
            unsubscribes: Optional[int]=None
    ):
        self.id=id
        self.name=name
        self.description=description
        self.is_default=is_default
        self.unsubscribes=unsubscribes

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_default": self.is_default,
            "unsubscribes": self.unsubscribes
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SuppressionGroup(
            id=payload.get('id'),
            name=payload.get('name'),
            description=payload.get('description'),
            is_default=payload.get('is_default'),
            unsubscribes=payload.get('unsubscribes')
        ) 

