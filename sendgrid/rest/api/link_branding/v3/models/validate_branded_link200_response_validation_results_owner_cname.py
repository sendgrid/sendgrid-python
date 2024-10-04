from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.link_branding.v3.models.valid2 import Valid2


class ValidateBrandedLink200ResponseValidationResultsOwnerCname:
    def __init__(self, valid: Optional[Valid2] = None, reason: Optional[str] = None):
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
        return ValidateBrandedLink200ResponseValidationResultsOwnerCname(
            valid=payload.get("valid"), reason=payload.get("reason")
        )
