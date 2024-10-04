from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class SendACampaignResponse:
    def __init__(self, id: Optional[int] = None, status: Optional[str] = None):
        self.id = id
        self.status = status

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"id": self.id, "status": self.status}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendACampaignResponse(id=payload.get("id"), status=payload.get("status"))
