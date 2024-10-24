from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class DeleteIpFromIpPool404Response:
    def __init__(
            self,
            error: Optional[str]=None
    ):
        self.error=error

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "error": self.error
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return DeleteIpFromIpPool404Response(
            error=payload.get('error')
        ) 
