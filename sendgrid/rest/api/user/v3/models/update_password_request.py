from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class UpdatePasswordRequest:
    def __init__(
        self, new_password: Optional[str] = None, old_password: Optional[str] = None
    ):
        self.new_password = new_password
        self.old_password = old_password

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "new_password": self.new_password,
                "old_password": self.old_password,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdatePasswordRequest(
            new_password=payload.get("new_password"),
            old_password=payload.get("old_password"),
        )
