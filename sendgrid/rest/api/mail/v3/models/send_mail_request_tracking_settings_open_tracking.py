from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class SendMailRequestTrackingSettingsOpenTracking:
    def __init__(
        self, enable: Optional[bool] = None, substitution_tag: Optional[str] = None
    ):
        self.enable = enable
        self.substitution_tag = substitution_tag

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "enable": self.enable,
                "substitution_tag": self.substitution_tag,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendMailRequestTrackingSettingsOpenTracking(
            enable=payload.get("enable"),
            substitution_tag=payload.get("substitution_tag"),
        )
