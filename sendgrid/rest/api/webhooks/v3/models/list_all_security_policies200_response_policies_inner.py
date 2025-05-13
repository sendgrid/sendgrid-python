from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.webhooks.v3.models.list_all_security_policies200_response_policies_inner_oauth import ListAllSecurityPolicies200ResponsePoliciesInnerOauth
from sendgrid.rest.api.webhooks.v3.models.list_all_security_policies200_response_policies_inner_signature import ListAllSecurityPolicies200ResponsePoliciesInnerSignature



class ListAllSecurityPolicies200ResponsePoliciesInner:
    def __init__(
            self,
            id: Optional[str]=None,
            name: Optional[str]=None,
            oauth: Optional[ListAllSecurityPolicies200ResponsePoliciesInnerOauth]=None,
            signature: Optional[ListAllSecurityPolicies200ResponsePoliciesInnerSignature]=None
    ):
        self.id=id
        self.name=name
        self.oauth=oauth
        self.signature=signature

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "name": self.name,
            "oauth": self.oauth,
            "signature": self.signature
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListAllSecurityPolicies200ResponsePoliciesInner(
            id=payload.get('id'),
            name=payload.get('name'),
            oauth=payload.get('oauth'),
            signature=payload.get('signature')
        ) 

