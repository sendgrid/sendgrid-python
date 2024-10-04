from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.sso.v3.models.sso_teammates_restricted_subuser_response_props_subuser_access_inner import (
    SsoTeammatesRestrictedSubuserResponsePropsSubuserAccessInner,
)


class PostSsoTeammates201:
    def __init__(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
        is_admin: Optional[bool] = None,
        is_sso: Optional[bool] = None,
        scopes: Optional[List[str]] = None,
        has_restricted_subuser_access: Optional[bool] = None,
        subuser_access: Optional[
            List[SsoTeammatesRestrictedSubuserResponsePropsSubuserAccessInner]
        ] = None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.is_sso = is_sso
        self.scopes = scopes
        self.has_restricted_subuser_access = has_restricted_subuser_access
        self.subuser_access = subuser_access

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email,
                "is_admin": self.is_admin,
                "is_sso": self.is_sso,
                "scopes": self.scopes,
                "has_restricted_subuser_access": self.has_restricted_subuser_access,
                "subuser_access": self.subuser_access,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return PostSsoTeammates201(
            first_name=payload.get("first_name"),
            last_name=payload.get("last_name"),
            email=payload.get("email"),
            is_admin=payload.get("is_admin"),
            is_sso=payload.get("is_sso"),
            scopes=payload.get("scopes"),
            has_restricted_subuser_access=payload.get("has_restricted_subuser_access"),
            subuser_access=payload.get("subuser_access"),
        )
