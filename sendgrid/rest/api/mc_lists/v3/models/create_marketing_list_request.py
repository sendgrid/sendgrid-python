from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class CreateMarketingListRequest:
    def __init__(self, name: Optional[str] = None):
        self.name = name

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"name": self.name}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CreateMarketingListRequest(name=payload.get("name"))
