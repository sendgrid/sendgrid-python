from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class UpdateAlertRequest:
    def __init__(
        self,
        email_to: Optional[str] = None,
        frequency: Optional[str] = None,
        percentage: Optional[int] = None,
    ):
        self.email_to = email_to
        self.frequency = frequency
        self.percentage = percentage

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "email_to": self.email_to,
                "frequency": self.frequency,
                "percentage": self.percentage,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateAlertRequest(
            email_to=payload.get("email_to"),
            frequency=payload.get("frequency"),
            percentage=payload.get("percentage"),
        )
