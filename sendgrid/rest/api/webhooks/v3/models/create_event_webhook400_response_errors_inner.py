from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class CreateEventWebhook400ResponseErrorsInner:
    def __init__(
        self,
        id: Optional[str] = None,
        message: Optional[str] = None,
        url: Optional[str] = None,
    ):
        self.id = id
        self.message = message
        self.url = url

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "message": self.message,
                "url": self.url,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CreateEventWebhook400ResponseErrorsInner(
            id=payload.get("id"), message=payload.get("message"), url=payload.get("url")
        )
