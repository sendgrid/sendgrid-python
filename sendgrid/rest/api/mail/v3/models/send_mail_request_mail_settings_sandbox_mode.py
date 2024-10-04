from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class SendMailRequestMailSettingsSandboxMode:
    def __init__(self, enable: Optional[bool] = None):
        self.enable = enable

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"enable": self.enable}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendMailRequestMailSettingsSandboxMode(enable=payload.get("enable"))
