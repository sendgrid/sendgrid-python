from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.domain_authentication.v3.models.validate_authenticated_domain200_response_validation_results_dkim1 import (
    ValidateAuthenticatedDomain200ResponseValidationResultsDkim1,
)
from sendgrid.rest.api.domain_authentication.v3.models.validate_authenticated_domain200_response_validation_results_mail_cname import (
    ValidateAuthenticatedDomain200ResponseValidationResultsMailCname,
)
from sendgrid.rest.api.domain_authentication.v3.models.validate_authenticated_domain200_response_validation_results_spf import (
    ValidateAuthenticatedDomain200ResponseValidationResultsSpf,
)


class ValidateAuthenticatedDomain200ResponseValidationResults:
    def __init__(
        self,
        mail_cname: Optional[
            ValidateAuthenticatedDomain200ResponseValidationResultsMailCname
        ] = None,
        dkim1: Optional[
            ValidateAuthenticatedDomain200ResponseValidationResultsDkim1
        ] = None,
        dkim2: Optional[
            ValidateAuthenticatedDomain200ResponseValidationResultsDkim1
        ] = None,
        spf: Optional[
            ValidateAuthenticatedDomain200ResponseValidationResultsSpf
        ] = None,
    ):
        self.mail_cname = mail_cname
        self.dkim1 = dkim1
        self.dkim2 = dkim2
        self.spf = spf

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "mail_cname": self.mail_cname,
                "dkim1": self.dkim1,
                "dkim2": self.dkim2,
                "spf": self.spf,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ValidateAuthenticatedDomain200ResponseValidationResults(
            mail_cname=payload.get("mail_cname"),
            dkim1=payload.get("dkim1"),
            dkim2=payload.get("dkim2"),
            spf=payload.get("spf"),
        )
