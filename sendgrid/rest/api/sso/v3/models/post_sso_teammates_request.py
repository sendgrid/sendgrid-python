from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.sso.v3.models.persona import Persona
from sendgrid.rest.api.sso.v3.models.sso_teammates_base_request_props_subuser_access_inner import SsoTeammatesBaseRequestPropsSubuserAccessInner



class PostSsoTeammatesRequest:
    def __init__(
            self,
            email: Optional[str]=None,
            first_name: Optional[str]=None,
            last_name: Optional[str]=None,
            is_admin: Optional[bool]=None,
            persona: Optional[Persona]=None,
            scopes: Optional[List[str]]=None,
            has_restricted_subuser_access: Optional[bool]=None,
            subuser_access: Optional[List[SsoTeammatesBaseRequestPropsSubuserAccessInner]]=None
    ):
        self.email=email
        self.first_name=first_name
        self.last_name=last_name
        self.is_admin=is_admin
        self.persona=persona
        self.scopes=scopes
        self.has_restricted_subuser_access=has_restricted_subuser_access
        self.subuser_access=subuser_access

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_admin": self.is_admin,
            "persona": self.persona,
            "scopes": self.scopes,
            "has_restricted_subuser_access": self.has_restricted_subuser_access,
            "subuser_access": self.subuser_access
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return PostSsoTeammatesRequest(
            email=payload.get('email'),
            first_name=payload.get('first_name'),
            last_name=payload.get('last_name'),
            is_admin=payload.get('is_admin'),
            persona=payload.get('persona'),
            scopes=payload.get('scopes'),
            has_restricted_subuser_access=payload.get('has_restricted_subuser_access'),
            subuser_access=payload.get('subuser_access')
        ) 

