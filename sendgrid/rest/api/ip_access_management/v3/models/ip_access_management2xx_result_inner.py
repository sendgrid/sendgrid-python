from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class IpAccessManagement2xxResultInner:
    def __init__(
            self,
            id: Optional[int]=None,
            ip: Optional[str]=None,
            created_at: Optional[int]=None,
            updated_at: Optional[int]=None
    ):
        self.id=id
        self.ip=ip
        self.created_at=created_at
        self.updated_at=updated_at

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "ip": self.ip,
            "created_at": self.created_at,
            "updated_at": self.updated_at
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return IpAccessManagement2xxResultInner(
            id=payload.get('id'),
            ip=payload.get('ip'),
            created_at=payload.get('created_at'),
            updated_at=payload.get('updated_at')
        ) 

