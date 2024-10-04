from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ListAllAuthenticatedDomainWithUser200ResponseInnerDnsMailCname:
    def __init__(
            self,
            valid: Optional[bool]=None,
            type: Optional[str]=None,
            host: Optional[str]=None,
            data: Optional[str]=None
    ):
        self.valid=valid
        self.type=type
        self.host=host
        self.data=data

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "valid": self.valid,
            "type": self.type,
            "host": self.host,
            "data": self.data
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListAllAuthenticatedDomainWithUser200ResponseInnerDnsMailCname(
            valid=payload.get('valid'),
            type=payload.get('type'),
            host=payload.get('host'),
            data=payload.get('data')
        ) 

