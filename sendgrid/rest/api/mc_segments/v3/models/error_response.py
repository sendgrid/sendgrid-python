from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_segments.v3.models.error_response_errors_inner import (
    ErrorResponseErrorsInner,
)


class ErrorResponse:
    def __init__(
        self,
        errors: Optional[List[ErrorResponseErrorsInner]] = None,
        id: Optional[str] = None,
    ):
        self.errors = errors
        self.id = id

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"errors": self.errors, "id": self.id}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ErrorResponse(errors=payload.get("errors"), id=payload.get("id"))
