from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListPendingTeammate200ResponseResultInner:
    def __init__(
        self,
        email: Optional[str] = None,
        scopes: Optional[List[str]] = None,
        is_admin: Optional[bool] = None,
        token: Optional[str] = None,
        expiration_date: Optional[int] = None,
    ):
        self.email = email
        self.scopes = scopes
        self.is_admin = is_admin
        self.token = token
        self.expiration_date = expiration_date

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "email": self.email,
                "scopes": self.scopes,
                "is_admin": self.is_admin,
                "token": self.token,
                "expiration_date": self.expiration_date,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListPendingTeammate200ResponseResultInner(
            email=payload.get("email"),
            scopes=payload.get("scopes"),
            is_admin=payload.get("is_admin"),
            token=payload.get("token"),
            expiration_date=payload.get("expiration_date"),
        )
