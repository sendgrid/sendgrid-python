from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class UpdateIpPool200Response:
    def __init__(
            self,
            name: Optional[str]=None,
            id: Optional[str]=None
    ):
        self.name=name
        self.id=id

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "name": self.name,
            "id": self.id
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateIpPool200Response(
            name=payload.get('name'),
            id=payload.get('id')
        ) 
