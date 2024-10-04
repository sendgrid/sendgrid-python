from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class SpamReportsResponseInner:
    def __init__(
        self,
        created: Optional[int] = None,
        email: Optional[str] = None,
        ip: Optional[str] = None,
    ):
        self.created = created
        self.email = email
        self.ip = ip

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "created": self.created,
                "email": self.email,
                "ip": self.ip,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SpamReportsResponseInner(
            created=payload.get("created"),
            email=payload.get("email"),
            ip=payload.get("ip"),
        )
