from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class GetAsmSuppression200ResponseSuppressionsInner:
    def __init__(
            self,
            description: Optional[str]=None,
            id: Optional[int]=None,
            is_default: Optional[bool]=None,
            name: Optional[str]=None,
            suppressed: Optional[bool]=None
    ):
        self.description=description
        self.id=id
        self.is_default=is_default
        self.name=name
        self.suppressed=suppressed

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "description": self.description,
            "id": self.id,
            "is_default": self.is_default,
            "name": self.name,
            "suppressed": self.suppressed
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetAsmSuppression200ResponseSuppressionsInner(
            description=payload.get('description'),
            id=payload.get('id'),
            is_default=payload.get('is_default'),
            name=payload.get('name'),
            suppressed=payload.get('suppressed')
        ) 

