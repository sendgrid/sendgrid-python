from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListUsername200Response:
    def __init__(self, username: Optional[str] = None, user_id: Optional[int] = None):
        self.username = username
        self.user_id = user_id

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "username": self.username,
                "user_id": self.user_id,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListUsername200Response(
            username=payload.get("username"), user_id=payload.get("user_id")
        )
