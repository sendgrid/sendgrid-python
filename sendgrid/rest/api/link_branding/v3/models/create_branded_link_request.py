from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.link_branding.v3.models.default import Default
from sendgrid.rest.api.link_branding.v3.models.region import Region


class CreateBrandedLinkRequest:
    def __init__(
        self,
        domain: Optional[str] = None,
        subdomain: Optional[str] = None,
        default: Optional[Default] = None,
        region: Optional[Region] = None,
    ):
        self.domain = domain
        self.subdomain = subdomain
        self.default = default
        self.region = region

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "domain": self.domain,
                "subdomain": self.subdomain,
                "default": self.default,
                "region": self.region,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CreateBrandedLinkRequest(
            domain=payload.get("domain"),
            subdomain=payload.get("subdomain"),
            default=payload.get("default"),
            region=payload.get("region"),
        )
