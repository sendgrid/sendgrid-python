from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_contacts.v3.models.identifier_type import IdentifierType



class DeleteContactIdentifierRequest:
    def __init__(
            self,
            identifier_type: Optional[IdentifierType]=None,
            identifier_value: Optional[str]=None
    ):
        self.identifier_type=identifier_type
        self.identifier_value=identifier_value

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "identifier_type": self.identifier_type,
            "identifier_value": self.identifier_value
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return DeleteContactIdentifierRequest(
            identifier_type=payload.get('identifier_type'),
            identifier_value=payload.get('identifier_value')
        ) 

