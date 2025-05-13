from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class DeleteSecurityPolicy200Response:
    def __init__(
            self,
            policy: Optional[str]=None
    ):
        self.policy=policy

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "policy": self.policy
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return DeleteSecurityPolicy200Response(
            policy=payload.get('policy')
        ) 

