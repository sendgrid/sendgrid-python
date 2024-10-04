from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class Id:
    def __init__(
            self,
            integration_id: Optional[str]=None
    ):
        self.integration_id=integration_id

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "integration_id": self.integration_id
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return Id(
            integration_id=payload.get('integration_id')
        ) 

