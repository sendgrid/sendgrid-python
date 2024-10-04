from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class UpdateRecipientRequestInner:
    def __init__(
        self,
        email: Optional[str] = None,
        last_name: Optional[str] = None,
        first_name: Optional[str] = None,
    ):
        self.email = email
        self.last_name = last_name
        self.first_name = first_name

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "email": self.email,
                "last_name": self.last_name,
                "first_name": self.first_name,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateRecipientRequestInner(
            email=payload.get("email"),
            last_name=payload.get("last_name"),
            first_name=payload.get("first_name"),
        )
