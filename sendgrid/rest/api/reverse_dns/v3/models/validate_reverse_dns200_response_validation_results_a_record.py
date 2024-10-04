from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.reverse_dns.v3.models.valid1 import Valid1



class ValidateReverseDns200ResponseValidationResultsARecord:
    def __init__(
            self,
            valid: Optional[Valid1]=None,
            reason: Optional[str]=None
    ):
        self.valid=valid
        self.reason=reason

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "valid": self.valid,
            "reason": self.reason
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ValidateReverseDns200ResponseValidationResultsARecord(
            valid=payload.get('valid'),
            reason=payload.get('reason')
        ) 

