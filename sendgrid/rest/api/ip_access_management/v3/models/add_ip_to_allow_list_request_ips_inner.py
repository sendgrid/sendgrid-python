from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class AddIpToAllowListRequestIpsInner:
    def __init__(self, ip: Optional[str] = None):
        self.ip = ip

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"ip": self.ip}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AddIpToAllowListRequestIpsInner(ip=payload.get("ip"))
