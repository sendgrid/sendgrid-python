from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.webhooks.v3.models.update_security_policy200_response_policy import UpdateSecurityPolicy200ResponsePolicy



class UpdateSecurityPolicy200Response:
    def __init__(
            self,
            policy: Optional[UpdateSecurityPolicy200ResponsePolicy]=None
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
        return UpdateSecurityPolicy200Response(
            policy=payload.get('policy')
        ) 

