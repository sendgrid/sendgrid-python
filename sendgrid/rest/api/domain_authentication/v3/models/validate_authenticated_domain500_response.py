from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.domain_authentication.v3.models.validate_authenticated_domain500_response_errors_inner import (
    ValidateAuthenticatedDomain500ResponseErrorsInner,
)


class ValidateAuthenticatedDomain500Response:
    def __init__(
        self,
        errors: Optional[
            List[ValidateAuthenticatedDomain500ResponseErrorsInner]
        ] = None,
    ):
        self.errors = errors

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"errors": self.errors}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ValidateAuthenticatedDomain500Response(errors=payload.get("errors"))
