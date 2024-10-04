from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class AddIp201ResponseIpsInner:
    def __init__(self, ip: Optional[str] = None, subusers: Optional[List[str]] = None):
        self.ip = ip
        self.subusers = subusers

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"ip": self.ip, "subusers": self.subusers}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AddIp201ResponseIpsInner(
            ip=payload.get("ip"), subusers=payload.get("subusers")
        )
