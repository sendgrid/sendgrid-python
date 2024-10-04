from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class DeleteAllowedIpsRequest:
    def __init__(self, ids: Optional[List[int]] = None):
        self.ids = ids

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"ids": self.ids}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return DeleteAllowedIpsRequest(ids=payload.get("ids"))
