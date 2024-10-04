from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListStatus200ResponseStatusInner:
    def __init__(self, id: Optional[str] = None, value: Optional[str] = None):
        self.id = id
        self.value = value

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"id": self.id, "value": self.value}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListStatus200ResponseStatusInner(
            id=payload.get("id"), value=payload.get("value")
        )
