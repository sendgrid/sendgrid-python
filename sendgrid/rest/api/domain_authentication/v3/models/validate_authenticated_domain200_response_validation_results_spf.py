from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ValidateAuthenticatedDomain200ResponseValidationResultsSpf:
    def __init__(self, valid: Optional[bool] = None, reason: Optional[str] = None):
        self.valid = valid
        self.reason = reason

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"valid": self.valid, "reason": self.reason}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ValidateAuthenticatedDomain200ResponseValidationResultsSpf(
            valid=payload.get("valid"), reason=payload.get("reason")
        )
