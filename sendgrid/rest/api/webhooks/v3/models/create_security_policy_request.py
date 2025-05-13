from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.webhooks.v3.models.create_security_policy_request_oauth import CreateSecurityPolicyRequestOauth
from sendgrid.rest.api.webhooks.v3.models.create_security_policy_request_signature import CreateSecurityPolicyRequestSignature



class CreateSecurityPolicyRequest:
    def __init__(
            self,
            name: Optional[str]=None,
            oauth: Optional[CreateSecurityPolicyRequestOauth]=None,
            signature: Optional[CreateSecurityPolicyRequestSignature]=None
    ):
        self.name=name
        self.oauth=oauth
        self.signature=signature

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "name": self.name,
            "oauth": self.oauth,
            "signature": self.signature
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CreateSecurityPolicyRequest(
            name=payload.get('name'),
            oauth=payload.get('oauth'),
            signature=payload.get('signature')
        ) 

