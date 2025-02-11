from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.sso.v3.models.sso_teammates_restricted_subuser_response_props_subuser_access_inner import SsoTeammatesRestrictedSubuserResponsePropsSubuserAccessInner



class SsoTeammatesRestrictedSubuserResponseProps:
    def __init__(
            self,
            has_restricted_subuser_access: Optional[bool]=None,
            subuser_access: Optional[List[SsoTeammatesRestrictedSubuserResponsePropsSubuserAccessInner]]=None
    ):
        self.has_restricted_subuser_access=has_restricted_subuser_access
        self.subuser_access=subuser_access

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "has_restricted_subuser_access": self.has_restricted_subuser_access,
            "subuser_access": self.subuser_access
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SsoTeammatesRestrictedSubuserResponseProps(
            has_restricted_subuser_access=payload.get('has_restricted_subuser_access'),
            subuser_access=payload.get('subuser_access')
        ) 

