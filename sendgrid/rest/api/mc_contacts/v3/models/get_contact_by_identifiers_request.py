from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class GetContactByIdentifiersRequest:
    def __init__(
            self,
            identifiers: Optional[List[str]]=None
    ):
        self.identifiers=identifiers

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "identifiers": self.identifiers
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetContactByIdentifiersRequest(
            identifiers=payload.get('identifiers')
        ) 

