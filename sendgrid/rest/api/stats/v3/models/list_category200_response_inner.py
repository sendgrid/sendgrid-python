from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListCategory200ResponseInner:
    def __init__(self, category: Optional[str] = None):
        self.category = category

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"category": self.category}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListCategory200ResponseInner(category=payload.get("category"))
