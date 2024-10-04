from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.domain_authentication.v3.models.authenticated_domain_spf_dns_dkim import (
    AuthenticatedDomainSpfDnsDkim,
)
from sendgrid.rest.api.domain_authentication.v3.models.authenticated_domain_spf_dns_domain_spf import (
    AuthenticatedDomainSpfDnsDomainSpf,
)
from sendgrid.rest.api.domain_authentication.v3.models.authenticated_domain_spf_dns_mail_server import (
    AuthenticatedDomainSpfDnsMailServer,
)
from sendgrid.rest.api.domain_authentication.v3.models.authenticated_domain_spf_dns_subdomain_spf import (
    AuthenticatedDomainSpfDnsSubdomainSpf,
)


class AuthenticatedDomainSpfDns:
    def __init__(
        self,
        mail_server: Optional[AuthenticatedDomainSpfDnsMailServer] = None,
        subdomain_spf: Optional[AuthenticatedDomainSpfDnsSubdomainSpf] = None,
        domain_spf: Optional[AuthenticatedDomainSpfDnsDomainSpf] = None,
        dkim: Optional[AuthenticatedDomainSpfDnsDkim] = None,
    ):
        self.mail_server = mail_server
        self.subdomain_spf = subdomain_spf
        self.domain_spf = domain_spf
        self.dkim = dkim

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "mail_server": self.mail_server,
                "subdomain_spf": self.subdomain_spf,
                "domain_spf": self.domain_spf,
                "dkim": self.dkim,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AuthenticatedDomainSpfDns(
            mail_server=payload.get("mail_server"),
            subdomain_spf=payload.get("subdomain_spf"),
            domain_spf=payload.get("domain_spf"),
            dkim=payload.get("dkim"),
        )
