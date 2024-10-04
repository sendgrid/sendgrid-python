from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class SelfMetadata:
    def __init__(self, var_self: Optional[str] = None):
        self.var_self = var_self

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"self": self.var_self}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SelfMetadata(var_self=payload.get("self"))
