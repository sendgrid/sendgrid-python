from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ContactRequestCustomFields:
    def __init__(self, w1: Optional[str] = None):
        self.w1 = w1

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"w1": self.w1}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactRequestCustomFields(w1=payload.get("w1"))
