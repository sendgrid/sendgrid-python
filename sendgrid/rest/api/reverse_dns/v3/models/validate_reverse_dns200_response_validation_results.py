from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.reverse_dns.v3.models.validate_reverse_dns200_response_validation_results_a_record import ValidateReverseDns200ResponseValidationResultsARecord



class ValidateReverseDns200ResponseValidationResults:
    def __init__(
            self,
            a_record: Optional[ValidateReverseDns200ResponseValidationResultsARecord]=None
    ):
        self.a_record=a_record

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "a_record": self.a_record
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ValidateReverseDns200ResponseValidationResults(
            a_record=payload.get('a_record')
        ) 

