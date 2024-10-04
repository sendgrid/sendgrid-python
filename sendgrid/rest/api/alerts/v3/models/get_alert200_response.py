from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.alerts.v3.models.type2 import Type2


class GetAlert200Response:
    def __init__(
        self,
        created_at: Optional[int] = None,
        email_to: Optional[str] = None,
        frequency: Optional[str] = None,
        id: Optional[int] = None,
        type: Optional[Type2] = None,
        updated_at: Optional[int] = None,
        percentage: Optional[int] = None,
    ):
        self.created_at = created_at
        self.email_to = email_to
        self.frequency = frequency
        self.id = id
        self.type = type
        self.updated_at = updated_at
        self.percentage = percentage

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "created_at": self.created_at,
                "email_to": self.email_to,
                "frequency": self.frequency,
                "id": self.id,
                "type": self.type,
                "updated_at": self.updated_at,
                "percentage": self.percentage,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetAlert200Response(
            created_at=payload.get("created_at"),
            email_to=payload.get("email_to"),
            frequency=payload.get("frequency"),
            id=payload.get("id"),
            type=payload.get("type"),
            updated_at=payload.get("updated_at"),
            percentage=payload.get("percentage"),
        )
