from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SsoTeammatesBaseResponseProps:
    def __init__(
            self,
            first_name: Optional[str]=None,
            last_name: Optional[str]=None,
            email: Optional[str]=None,
            is_admin: Optional[bool]=None,
            is_sso: Optional[bool]=None,
            scopes: Optional[List[str]]=None
    ):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.is_admin=is_admin
        self.is_sso=is_sso
        self.scopes=scopes

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin,
            "is_sso": self.is_sso,
            "scopes": self.scopes
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SsoTeammatesBaseResponseProps(
            first_name=payload.get('first_name'),
            last_name=payload.get('last_name'),
            email=payload.get('email'),
            is_admin=payload.get('is_admin'),
            is_sso=payload.get('is_sso'),
            scopes=payload.get('scopes')
        ) 

