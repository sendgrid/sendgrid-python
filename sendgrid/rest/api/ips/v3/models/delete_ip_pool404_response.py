from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class DeleteIpPool404Response:
    def __init__(self, error: Optional[str] = None):
        self.error = error

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"error": self.error}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return DeleteIpPool404Response(error=payload.get("error"))
