from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class EmailDnsRecord400ResponseErrors:
    def __init__(self, error: Optional[str] = None, field: Optional[str] = None):
        self.error = error
        self.field = field

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"error": self.error, "field": self.field}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return EmailDnsRecord400ResponseErrors(
            error=payload.get("error"), field=payload.get("field")
        )
