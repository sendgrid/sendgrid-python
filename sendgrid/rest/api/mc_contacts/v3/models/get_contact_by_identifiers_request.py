from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class GetContactByIdentifiersRequest:
    def __init__(self, identifiers: Optional[List[str]] = None):
        self.identifiers = identifiers

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"identifiers": self.identifiers}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetContactByIdentifiersRequest(identifiers=payload.get("identifiers"))
