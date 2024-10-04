from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.scheduled_sends.v3.models.status1 import Status1


class UpdateScheduledSendRequest:
    def __init__(self, status: Optional[Status1] = None):
        self.status = status

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"status": self.status}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateScheduledSendRequest(status=payload.get("status"))
