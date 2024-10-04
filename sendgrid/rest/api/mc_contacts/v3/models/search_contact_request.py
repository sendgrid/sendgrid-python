from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class SearchContactRequest:
    def __init__(self, query: Optional[str] = None):
        self.query = query

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"query": self.query}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SearchContactRequest(query=payload.get("query"))
