from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.domain_authentication.v3.models.validate_authenticated_domain200_response_validation_results import (
    ValidateAuthenticatedDomain200ResponseValidationResults,
)


class ValidateAuthenticatedDomain200Response:
    def __init__(
        self,
        id: Optional[int] = None,
        valid: Optional[bool] = None,
        validation_results: Optional[
            ValidateAuthenticatedDomain200ResponseValidationResults
        ] = None,
    ):
        self.id = id
        self.valid = valid
        self.validation_results = validation_results

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "valid": self.valid,
                "validation_results": self.validation_results,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ValidateAuthenticatedDomain200Response(
            id=payload.get("id"),
            valid=payload.get("valid"),
            validation_results=payload.get("validation_results"),
        )
