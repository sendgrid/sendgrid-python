from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ListAsmSuppression200ResponseInner:
    def __init__(
            self,
            email: Optional[str]=None,
            group_id: Optional[int]=None,
            group_name: Optional[str]=None,
            created_at: Optional[int]=None
    ):
        self.email=email
        self.group_id=group_id
        self.group_name=group_name
        self.created_at=created_at

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "email": self.email,
            "group_id": self.group_id,
            "group_name": self.group_name,
            "created_at": self.created_at
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListAsmSuppression200ResponseInner(
            email=payload.get('email'),
            group_id=payload.get('group_id'),
            group_name=payload.get('group_name'),
            created_at=payload.get('created_at')
        ) 

