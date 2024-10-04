from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class SetUpReverseDnsRequest:
    def __init__(
        self,
        ip: Optional[str] = None,
        subdomain: Optional[str] = None,
        domain: Optional[str] = None,
    ):
        self.ip = ip
        self.subdomain = subdomain
        self.domain = domain

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "ip": self.ip,
                "subdomain": self.subdomain,
                "domain": self.domain,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SetUpReverseDnsRequest(
            ip=payload.get("ip"),
            subdomain=payload.get("subdomain"),
            domain=payload.get("domain"),
        )
