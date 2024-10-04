from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ParseSetting:
    def __init__(
        self,
        url: Optional[str] = None,
        hostname: Optional[str] = None,
        spam_check: Optional[bool] = None,
        send_raw: Optional[bool] = None,
    ):
        self.url = url
        self.hostname = hostname
        self.spam_check = spam_check
        self.send_raw = send_raw

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "url": self.url,
                "hostname": self.hostname,
                "spam_check": self.spam_check,
                "send_raw": self.send_raw,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ParseSetting(
            url=payload.get("url"),
            hostname=payload.get("hostname"),
            spam_check=payload.get("spam_check"),
            send_raw=payload.get("send_raw"),
        )
