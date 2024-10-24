from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ListScope200Response:
    def __init__(
            self,
            scopes: Optional[List[str]]=None
    ):
        self.scopes=scopes

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "scopes": self.scopes
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListScope200Response(
            scopes=payload.get('scopes')
        ) 

