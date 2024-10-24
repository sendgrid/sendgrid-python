from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class AddIpToAuthenticatedDomainRequest:
    def __init__(
            self,
            ip: Optional[str]=None
    ):
        self.ip=ip

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "ip": self.ip
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AddIpToAuthenticatedDomainRequest(
            ip=payload.get('ip')
        ) 

