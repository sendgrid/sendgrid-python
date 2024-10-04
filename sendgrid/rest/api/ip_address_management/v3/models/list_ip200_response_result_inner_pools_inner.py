from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListIp200ResponseResultInnerPoolsInner:
    def __init__(self, name: Optional[str] = None, id: Optional[str] = None):
        self.name = name
        self.id = id

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"name": self.name, "id": self.id}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListIp200ResponseResultInnerPoolsInner(
            name=payload.get("name"), id=payload.get("id")
        )
