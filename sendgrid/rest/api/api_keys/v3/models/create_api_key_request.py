from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class CreateApiKeyRequest:
    def __init__(
            self,
            name: Optional[str]=None,
            scopes: Optional[List[str]]=None
    ):
        self.name=name
        self.scopes=scopes

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "name": self.name,
            "scopes": self.scopes
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CreateApiKeyRequest(
            name=payload.get('name'),
            scopes=payload.get('scopes')
        ) 

