from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class GetIp200ResponsePoolsInner:
    def __init__(self, id: Optional[str] = None, name: Optional[str] = None):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"id": self.id, "name": self.name}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetIp200ResponsePoolsInner(
            id=payload.get("id"), name=payload.get("name")
        )
