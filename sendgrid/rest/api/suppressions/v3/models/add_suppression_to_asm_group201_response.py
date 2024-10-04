from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class AddSuppressionToAsmGroup201Response:
    def __init__(self, recipient_emails: Optional[List[str]] = None):
        self.recipient_emails = recipient_emails

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"recipient_emails": self.recipient_emails}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AddSuppressionToAsmGroup201Response(
            recipient_emails=payload.get("recipient_emails")
        )
