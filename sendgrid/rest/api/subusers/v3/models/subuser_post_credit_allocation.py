from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class SubuserPostCreditAllocation:
    def __init__(self, type: Optional[str] = None):
        self.type = type

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"type": self.type}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SubuserPostCreditAllocation(type=payload.get("type"))
