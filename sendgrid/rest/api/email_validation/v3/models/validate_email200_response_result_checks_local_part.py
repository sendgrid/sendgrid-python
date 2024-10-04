from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ValidateEmail200ResponseResultChecksLocalPart:
    def __init__(self, is_suspected_role_address: Optional[bool] = None):
        self.is_suspected_role_address = is_suspected_role_address

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "is_suspected_role_address": self.is_suspected_role_address
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ValidateEmail200ResponseResultChecksLocalPart(
            is_suspected_role_address=payload.get("is_suspected_role_address")
        )
