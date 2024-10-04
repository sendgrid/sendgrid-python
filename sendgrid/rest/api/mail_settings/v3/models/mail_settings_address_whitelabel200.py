from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class MailSettingsAddressWhitelabel200:
    def __init__(
        self, enabled: Optional[bool] = None, list: Optional[List[str]] = None
    ):
        self.enabled = enabled
        self.list = list

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"enabled": self.enabled, "list": self.list}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return MailSettingsAddressWhitelabel200(
            enabled=payload.get("enabled"), list=payload.get("list")
        )
