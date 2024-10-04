from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListAccessActivity200ResponseResultInner:
    def __init__(
        self,
        allowed: Optional[bool] = None,
        auth_method: Optional[str] = None,
        first_at: Optional[int] = None,
        ip: Optional[str] = None,
        last_at: Optional[int] = None,
        location: Optional[str] = None,
    ):
        self.allowed = allowed
        self.auth_method = auth_method
        self.first_at = first_at
        self.ip = ip
        self.last_at = last_at
        self.location = location

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "allowed": self.allowed,
                "auth_method": self.auth_method,
                "first_at": self.first_at,
                "ip": self.ip,
                "last_at": self.last_at,
                "location": self.location,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListAccessActivity200ResponseResultInner(
            allowed=payload.get("allowed"),
            auth_method=payload.get("auth_method"),
            first_at=payload.get("first_at"),
            ip=payload.get("ip"),
            last_at=payload.get("last_at"),
            location=payload.get("location"),
        )
