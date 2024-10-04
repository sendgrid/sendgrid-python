from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ValidateReverseDns500ResponseErrorsInner:
    def __init__(self, message: Optional[str] = None):
        self.message = message

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"message": self.message}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ValidateReverseDns500ResponseErrorsInner(message=payload.get("message"))
