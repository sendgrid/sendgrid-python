from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class CreateApiKey201Response:
    def __init__(
            self,
            api_key: Optional[str]=None,
            api_key_id: Optional[str]=None,
            name: Optional[str]=None,
            scopes: Optional[List[str]]=None
    ):
        self.api_key=api_key
        self.api_key_id=api_key_id
        self.name=name
        self.scopes=scopes

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "api_key": self.api_key,
            "api_key_id": self.api_key_id,
            "name": self.name,
            "scopes": self.scopes
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CreateApiKey201Response(
            api_key=payload.get('api_key'),
            api_key_id=payload.get('api_key_id'),
            name=payload.get('name'),
            scopes=payload.get('scopes')
        ) 

