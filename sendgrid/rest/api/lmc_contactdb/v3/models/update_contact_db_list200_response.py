from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class UpdateContactDbList200Response:
    def __init__(
        self,
        id: Optional[int] = None,
        name: Optional[str] = None,
        recipient_count: Optional[int] = None,
    ):
        self.id = id
        self.name = name
        self.recipient_count = recipient_count

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "name": self.name,
                "recipient_count": self.recipient_count,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateContactDbList200Response(
            id=payload.get("id"),
            name=payload.get("name"),
            recipient_count=payload.get("recipient_count"),
        )
