from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.subusers.v3.models.region2 import Region2


class Subuser:
    def __init__(
        self,
        disabled: Optional[bool] = None,
        id: Optional[float] = None,
        username: Optional[str] = None,
        email: Optional[str] = None,
        region: Optional[Region2] = None,
    ):
        self.disabled = disabled
        self.id = id
        self.username = username
        self.email = email
        self.region = region

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "disabled": self.disabled,
                "id": self.id,
                "username": self.username,
                "email": self.email,
                "region": self.region,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return Subuser(
            disabled=payload.get("disabled"),
            id=payload.get("id"),
            username=payload.get("username"),
            email=payload.get("email"),
            region=payload.get("region"),
        )
