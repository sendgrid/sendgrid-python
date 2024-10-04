from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListEmail200Response:
    def __init__(self, email: Optional[str] = None):
        self.email = email

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"email": self.email}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListEmail200Response(email=payload.get("email"))
