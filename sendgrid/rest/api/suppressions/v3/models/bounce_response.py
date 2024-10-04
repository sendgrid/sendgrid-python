from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class BounceResponse:
    def __init__(
        self,
        created: Optional[float] = None,
        email: Optional[str] = None,
        reason: Optional[str] = None,
        status: Optional[str] = None,
    ):
        self.created = created
        self.email = email
        self.reason = reason
        self.status = status

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "created": self.created,
                "email": self.email,
                "reason": self.reason,
                "status": self.status,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return BounceResponse(
            created=payload.get("created"),
            email=payload.get("email"),
            reason=payload.get("reason"),
            status=payload.get("status"),
        )
