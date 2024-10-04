from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.reverse_dns.v3.models.validate_reverse_dns500_response_errors_inner import ValidateReverseDns500ResponseErrorsInner



class ValidateReverseDns500Response:
    def __init__(
            self,
            errors: Optional[List[ValidateReverseDns500ResponseErrorsInner]]=None
    ):
        self.errors=errors

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "errors": self.errors
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ValidateReverseDns500Response(
            errors=payload.get('errors')
        ) 

