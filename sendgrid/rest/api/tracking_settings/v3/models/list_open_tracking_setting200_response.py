from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListOpenTrackingSetting200Response:
    def __init__(self, enabled: Optional[bool] = None):
        self.enabled = enabled

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"enabled": self.enabled}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListOpenTrackingSetting200Response(enabled=payload.get("enabled"))
