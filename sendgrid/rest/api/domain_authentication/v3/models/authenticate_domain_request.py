from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class AuthenticateDomainRequest:
    def __init__(
        self,
        domain: Optional[str] = None,
        subdomain: Optional[str] = None,
        username: Optional[str] = None,
        ips: Optional[List[str]] = None,
        custom_spf: Optional[bool] = None,
        default: Optional[bool] = None,
        automatic_security: Optional[bool] = None,
        custom_dkim_selector: Optional[str] = None,
        region: Optional[str] = None,
    ):
        self.domain = domain
        self.subdomain = subdomain
        self.username = username
        self.ips = ips
        self.custom_spf = custom_spf
        self.default = default
        self.automatic_security = automatic_security
        self.custom_dkim_selector = custom_dkim_selector
        self.region = region

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "domain": self.domain,
                "subdomain": self.subdomain,
                "username": self.username,
                "ips": self.ips,
                "custom_spf": self.custom_spf,
                "default": self.default,
                "automatic_security": self.automatic_security,
                "custom_dkim_selector": self.custom_dkim_selector,
                "region": self.region,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AuthenticateDomainRequest(
            domain=payload.get("domain"),
            subdomain=payload.get("subdomain"),
            username=payload.get("username"),
            ips=payload.get("ips"),
            custom_spf=payload.get("custom_spf"),
            default=payload.get("default"),
            automatic_security=payload.get("automatic_security"),
            custom_dkim_selector=payload.get("custom_dkim_selector"),
            region=payload.get("region"),
        )
