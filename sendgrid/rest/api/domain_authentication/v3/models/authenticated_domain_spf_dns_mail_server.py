from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class AuthenticatedDomainSpfDnsMailServer:
    def __init__(
        self,
        host: Optional[str] = None,
        type: Optional[str] = None,
        data: Optional[str] = None,
        valid: Optional[bool] = None,
    ):
        self.host = host
        self.type = type
        self.data = data
        self.valid = valid

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "host": self.host,
                "type": self.type,
                "data": self.data,
                "valid": self.valid,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AuthenticatedDomainSpfDnsMailServer(
            host=payload.get("host"),
            type=payload.get("type"),
            data=payload.get("data"),
            valid=payload.get("valid"),
        )
