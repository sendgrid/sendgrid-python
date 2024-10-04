from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class IpWarmup200Inner:
    def __init__(self, ip: Optional[str] = None, start_date: Optional[int] = None):
        self.ip = ip
        self.start_date = start_date

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"ip": self.ip, "start_date": self.start_date}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return IpWarmup200Inner(
            ip=payload.get("ip"), start_date=payload.get("start_date")
        )
