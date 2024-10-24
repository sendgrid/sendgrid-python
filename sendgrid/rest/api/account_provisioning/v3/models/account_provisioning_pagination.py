from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class AccountProvisioningPagination:
    def __init__(
            self,
            last: Optional[str]=None,
            example: Optional[object]=None
    ):
        self.last=last
        self.example=example

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "last": self.last,
            "example": self.example
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AccountProvisioningPagination(
            last=payload.get('last'),
            example=payload.get('example')
        ) 

