from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.sso.v3.models.sso_teammates_restricted_subuser_response_props_subuser_access_inner import (
    SsoTeammatesRestrictedSubuserResponsePropsSubuserAccessInner,
)
from sendgrid.rest.api.sso.v3.models.user_type import UserType


class PatchSsoTeammates200:
    def __init__(
        self,
        address: Optional[str] = None,
        address2: Optional[str] = None,
        city: Optional[str] = None,
        company: Optional[str] = None,
        country: Optional[str] = None,
        username: Optional[str] = None,
        phone: Optional[str] = None,
        state: Optional[str] = None,
        user_type: Optional[UserType] = None,
        website: Optional[str] = None,
        zip: Optional[str] = None,
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
        self.address = address
        self.address2 = address2
        self.city = city
        self.company = company
        self.country = country
        self.username = username
        self.phone = phone
        self.state = state
        self.user_type = user_type
        self.website = website
        self.zip = zip
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
                "address": self.address,
                "address2": self.address2,
                "city": self.city,
                "company": self.company,
                "country": self.country,
                "username": self.username,
                "phone": self.phone,
                "state": self.state,
                "user_type": self.user_type,
                "website": self.website,
                "zip": self.zip,
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
        return PatchSsoTeammates200(
            address=payload.get("address"),
            address2=payload.get("address2"),
            city=payload.get("city"),
            company=payload.get("company"),
            country=payload.get("country"),
            username=payload.get("username"),
            phone=payload.get("phone"),
            state=payload.get("state"),
            user_type=payload.get("user_type"),
            website=payload.get("website"),
            zip=payload.get("zip"),
            first_name=payload.get("first_name"),
            last_name=payload.get("last_name"),
            email=payload.get("email"),
            is_admin=payload.get("is_admin"),
            is_sso=payload.get("is_sso"),
            scopes=payload.get("scopes"),
            has_restricted_subuser_access=payload.get("has_restricted_subuser_access"),
            subuser_access=payload.get("subuser_access"),
        )
