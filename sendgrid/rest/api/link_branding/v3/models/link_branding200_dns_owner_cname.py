from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.link_branding.v3.models.type1 import Type1
from sendgrid.rest.api.link_branding.v3.models.valid5 import Valid5


class LinkBranding200DnsOwnerCname:
    def __init__(
        self,
        valid: Optional[Valid5] = None,
        type: Optional[Type1] = None,
        host: Optional[str] = None,
        data: Optional[str] = None,
    ):
        self.valid = valid
        self.type = type
        self.host = host
        self.data = data

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "valid": self.valid,
                "type": self.type,
                "host": self.host,
                "data": self.data,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return LinkBranding200DnsOwnerCname(
            valid=payload.get("valid"),
            type=payload.get("type"),
            host=payload.get("host"),
            data=payload.get("data"),
        )
