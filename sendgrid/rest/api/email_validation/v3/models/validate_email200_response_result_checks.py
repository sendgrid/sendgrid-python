from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.email_validation.v3.models.validate_email200_response_result_checks_additional import ValidateEmail200ResponseResultChecksAdditional
from sendgrid.rest.api.email_validation.v3.models.validate_email200_response_result_checks_domain import ValidateEmail200ResponseResultChecksDomain
from sendgrid.rest.api.email_validation.v3.models.validate_email200_response_result_checks_local_part import ValidateEmail200ResponseResultChecksLocalPart



class ValidateEmail200ResponseResultChecks:
    def __init__(
            self,
            domain: Optional[ValidateEmail200ResponseResultChecksDomain]=None,
            local_part: Optional[ValidateEmail200ResponseResultChecksLocalPart]=None,
            additional: Optional[ValidateEmail200ResponseResultChecksAdditional]=None
    ):
        self.domain=domain
        self.local_part=local_part
        self.additional=additional

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "domain": self.domain,
            "local_part": self.local_part,
            "additional": self.additional
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ValidateEmail200ResponseResultChecks(
            domain=payload.get('domain'),
            local_part=payload.get('local_part'),
            additional=payload.get('additional')
        ) 

