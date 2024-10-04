from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.domain_authentication.v3.models.list_all_authenticated_domain_with_user200_response_inner_dns_dkim1 import (
    ListAllAuthenticatedDomainWithUser200ResponseInnerDnsDkim1,
)
from sendgrid.rest.api.domain_authentication.v3.models.list_all_authenticated_domain_with_user200_response_inner_dns_mail_cname import (
    ListAllAuthenticatedDomainWithUser200ResponseInnerDnsMailCname,
)


class ListAllAuthenticatedDomainWithUser200ResponseInnerDns:
    def __init__(
        self,
        mail_cname: Optional[
            ListAllAuthenticatedDomainWithUser200ResponseInnerDnsMailCname
        ] = None,
        dkim1: Optional[
            ListAllAuthenticatedDomainWithUser200ResponseInnerDnsDkim1
        ] = None,
        dkim2: Optional[
            ListAllAuthenticatedDomainWithUser200ResponseInnerDnsDkim1
        ] = None,
    ):
        self.mail_cname = mail_cname
        self.dkim1 = dkim1
        self.dkim2 = dkim2

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "mail_cname": self.mail_cname,
                "dkim1": self.dkim1,
                "dkim2": self.dkim2,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListAllAuthenticatedDomainWithUser200ResponseInnerDns(
            mail_cname=payload.get("mail_cname"),
            dkim1=payload.get("dkim1"),
            dkim2=payload.get("dkim2"),
        )
