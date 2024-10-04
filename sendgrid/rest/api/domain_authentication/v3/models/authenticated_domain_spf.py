from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.domain_authentication.v3.models.authenticated_domain_spf_dns import (
    AuthenticatedDomainSpfDns,
)


class AuthenticatedDomainSpf:
    def __init__(
        self,
        id: Optional[int] = None,
        domain: Optional[str] = None,
        subdomain: Optional[str] = None,
        username: Optional[str] = None,
        user_id: Optional[int] = None,
        ips: Optional[List[object]] = None,
        custom_spf: Optional[bool] = None,
        default: Optional[bool] = None,
        legacy: Optional[bool] = None,
        automatic_security: Optional[bool] = None,
        valid: Optional[bool] = None,
        dns: Optional[AuthenticatedDomainSpfDns] = None,
    ):
        self.id = id
        self.domain = domain
        self.subdomain = subdomain
        self.username = username
        self.user_id = user_id
        self.ips = ips
        self.custom_spf = custom_spf
        self.default = default
        self.legacy = legacy
        self.automatic_security = automatic_security
        self.valid = valid
        self.dns = dns

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "domain": self.domain,
                "subdomain": self.subdomain,
                "username": self.username,
                "user_id": self.user_id,
                "ips": self.ips,
                "custom_spf": self.custom_spf,
                "default": self.default,
                "legacy": self.legacy,
                "automatic_security": self.automatic_security,
                "valid": self.valid,
                "dns": self.dns,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AuthenticatedDomainSpf(
            id=payload.get("id"),
            domain=payload.get("domain"),
            subdomain=payload.get("subdomain"),
            username=payload.get("username"),
            user_id=payload.get("user_id"),
            ips=payload.get("ips"),
            custom_spf=payload.get("custom_spf"),
            default=payload.get("default"),
            legacy=payload.get("legacy"),
            automatic_security=payload.get("automatic_security"),
            valid=payload.get("valid"),
            dns=payload.get("dns"),
        )
