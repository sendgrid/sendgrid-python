from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.reverse_dns.v3.models.valid import Valid
from sendgrid.rest.api.reverse_dns.v3.models.validate_reverse_dns200_response_validation_results import ValidateReverseDns200ResponseValidationResults



class ValidateReverseDns200Response:
    def __init__(
            self,
            id: Optional[int]=None,
            valid: Optional[Valid]=None,
            validation_results: Optional[ValidateReverseDns200ResponseValidationResults]=None
    ):
        self.id=id
        self.valid=valid
        self.validation_results=validation_results

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "valid": self.valid,
            "validation_results": self.validation_results
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ValidateReverseDns200Response(
            id=payload.get('id'),
            valid=payload.get('valid'),
            validation_results=payload.get('validation_results')
        ) 

