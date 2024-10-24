from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.user.v3.models.type import Type



class GETUserAccountResponse:
    def __init__(
            self,
            type: Optional[Type]=None,
            reputation: Optional[float]=None
    ):
        self.type=type
        self.reputation=reputation

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "type": self.type,
            "reputation": self.reputation
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GETUserAccountResponse(
            type=payload.get('type'),
            reputation=payload.get('reputation')
        ) 

