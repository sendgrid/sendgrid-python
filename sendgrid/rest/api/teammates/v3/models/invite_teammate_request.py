from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class InviteTeammateRequest:
    def __init__(
        self,
        email: Optional[str] = None,
        scopes: Optional[List[str]] = None,
        is_admin: Optional[bool] = None,
    ):
        self.email = email
        self.scopes = scopes
        self.is_admin = is_admin

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "email": self.email,
                "scopes": self.scopes,
                "is_admin": self.is_admin,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return InviteTeammateRequest(
            email=payload.get("email"),
            scopes=payload.get("scopes"),
            is_admin=payload.get("is_admin"),
        )
