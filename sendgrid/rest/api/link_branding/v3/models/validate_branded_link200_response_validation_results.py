from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.link_branding.v3.models.validate_branded_link200_response_validation_results_domain_cname import ValidateBrandedLink200ResponseValidationResultsDomainCname
from sendgrid.rest.api.link_branding.v3.models.validate_branded_link200_response_validation_results_owner_cname import ValidateBrandedLink200ResponseValidationResultsOwnerCname



class ValidateBrandedLink200ResponseValidationResults:
    def __init__(
            self,
            domain_cname: Optional[ValidateBrandedLink200ResponseValidationResultsDomainCname]=None,
            owner_cname: Optional[ValidateBrandedLink200ResponseValidationResultsOwnerCname]=None
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
        return ValidateBrandedLink200ResponseValidationResults(
            domain_cname=payload.get('domain_cname'),
            owner_cname=payload.get('owner_cname')
        ) 

