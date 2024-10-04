from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ErrorsSegmentV2ErrorsInner:
    def __init__(self, field: Optional[str] = None, message: Optional[str] = None):
        self.field = field
        self.message = message

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"field": self.field, "message": self.message}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ErrorsSegmentV2ErrorsInner(
            field=payload.get("field"), message=payload.get("message")
        )
