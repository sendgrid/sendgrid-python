from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.domain_authentication.v3.models.list_all_authenticated_domain_with_user200_response_inner_dns import ListAllAuthenticatedDomainWithUser200ResponseInnerDns



class AuthenticatedDomain:
    def __init__(
            self,
            id: Optional[float]=None,
            user_id: Optional[float]=None,
            subdomain: Optional[str]=None,
            domain: Optional[str]=None,
            username: Optional[str]=None,
            ips: Optional[List[str]]=None,
            custom_spf: Optional[bool]=None,
            default: Optional[bool]=None,
            legacy: Optional[bool]=None,
            automatic_security: Optional[bool]=None,
            valid: Optional[bool]=None,
            dns: Optional[ListAllAuthenticatedDomainWithUser200ResponseInnerDns]=None
    ):
        self.id=id
        self.user_id=user_id
        self.subdomain=subdomain
        self.domain=domain
        self.username=username
        self.ips=ips
        self.custom_spf=custom_spf
        self.default=default
        self.legacy=legacy
        self.automatic_security=automatic_security
        self.valid=valid
        self.dns=dns

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "user_id": self.user_id,
            "subdomain": self.subdomain,
            "domain": self.domain,
            "username": self.username,
            "ips": self.ips,
            "custom_spf": self.custom_spf,
            "default": self.default,
            "legacy": self.legacy,
            "automatic_security": self.automatic_security,
            "valid": self.valid,
            "dns": self.dns
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AuthenticatedDomain(
            id=payload.get('id'),
            user_id=payload.get('user_id'),
            subdomain=payload.get('subdomain'),
            domain=payload.get('domain'),
            username=payload.get('username'),
            ips=payload.get('ips'),
            custom_spf=payload.get('custom_spf'),
            default=payload.get('default'),
            legacy=payload.get('legacy'),
            automatic_security=payload.get('automatic_security'),
            valid=payload.get('valid'),
            dns=payload.get('dns')
        ) 

