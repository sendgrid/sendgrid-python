from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.webhooks.v3.models.list_all_security_policies200_response_policies_inner import ListAllSecurityPolicies200ResponsePoliciesInner



class ListAllSecurityPolicies200Response:
    def __init__(
            self,
            policies: Optional[List[ListAllSecurityPolicies200ResponsePoliciesInner]]=None
    ):
        self.policies=policies

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "policies": self.policies
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListAllSecurityPolicies200Response(
            policies=payload.get('policies')
        ) 

