from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class SendMailRequestMailSettingsFooter:
    def __init__(
        self,
        enable: Optional[bool] = None,
        text: Optional[str] = None,
        html: Optional[str] = None,
    ):
        self.enable = enable
        self.text = text
        self.html = html

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "enable": self.enable,
                "text": self.text,
                "html": self.html,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendMailRequestMailSettingsFooter(
            enable=payload.get("enable"),
            text=payload.get("text"),
            html=payload.get("html"),
        )
