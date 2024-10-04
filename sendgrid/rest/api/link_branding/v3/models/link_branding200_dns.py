from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.link_branding.v3.models.link_branding200_dns_domain_cname import LinkBranding200DnsDomainCname
from sendgrid.rest.api.link_branding.v3.models.link_branding200_dns_owner_cname import LinkBranding200DnsOwnerCname



class LinkBranding200Dns:
    def __init__(
            self,
            domain_cname: Optional[LinkBranding200DnsDomainCname]=None,
            owner_cname: Optional[LinkBranding200DnsOwnerCname]=None
    ):
        self.domain_cname=domain_cname
        self.owner_cname=owner_cname

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "domain_cname": self.domain_cname,
            "owner_cname": self.owner_cname
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return LinkBranding200Dns(
            domain_cname=payload.get('domain_cname'),
            owner_cname=payload.get('owner_cname')
        ) 

