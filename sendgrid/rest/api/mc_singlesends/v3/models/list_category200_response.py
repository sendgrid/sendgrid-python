from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListCategory200Response:
    def __init__(self, categories: Optional[List[str]] = None):
        self.categories = categories

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"categories": self.categories}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListCategory200Response(categories=payload.get("categories"))
