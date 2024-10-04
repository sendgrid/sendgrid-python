from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.link_branding.v3.models.default2 import Default2
from sendgrid.rest.api.link_branding.v3.models.legacy import Legacy
from sendgrid.rest.api.link_branding.v3.models.link_branding200_dns import LinkBranding200Dns
from sendgrid.rest.api.link_branding.v3.models.valid3 import Valid3



class LinkBranding200:
    def __init__(
            self,
            id: Optional[int]=None,
            domain: Optional[str]=None,
            subdomain: Optional[str]=None,
            username: Optional[str]=None,
            user_id: Optional[int]=None,
            default: Optional[Default2]=None,
            valid: Optional[Valid3]=None,
            legacy: Optional[Legacy]=None,
            dns: Optional[LinkBranding200Dns]=None
    ):
        self.id=id
        self.domain=domain
        self.subdomain=subdomain
        self.username=username
        self.user_id=user_id
        self.default=default
        self.valid=valid
        self.legacy=legacy
        self.dns=dns

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "domain": self.domain,
            "subdomain": self.subdomain,
            "username": self.username,
            "user_id": self.user_id,
            "default": self.default,
            "valid": self.valid,
            "legacy": self.legacy,
            "dns": self.dns
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return LinkBranding200(
            id=payload.get('id'),
            domain=payload.get('domain'),
            subdomain=payload.get('subdomain'),
            username=payload.get('username'),
            user_id=payload.get('user_id'),
            default=payload.get('default'),
            valid=payload.get('valid'),
            legacy=payload.get('legacy'),
            dns=payload.get('dns')
        ) 

