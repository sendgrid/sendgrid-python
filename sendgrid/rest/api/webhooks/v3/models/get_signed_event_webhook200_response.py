from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class GetSignedEventWebhook200Response:
    def __init__(
            self,
            id: Optional[str]=None,
            public_key: Optional[str]=None
    ):
        self.id=id
        self.public_key=public_key

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "public_key": self.public_key
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetSignedEventWebhook200Response(
            id=payload.get('id'),
            public_key=payload.get('public_key')
        ) 

