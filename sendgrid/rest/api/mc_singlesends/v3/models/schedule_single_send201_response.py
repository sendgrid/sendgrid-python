from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_singlesends.v3.models.status import Status


class ScheduleSingleSend201Response:
    def __init__(
        self, send_at: Optional[datetime] = None, status: Optional[Status] = None
    ):
        self.send_at = send_at
        self.status = status

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"send_at": self.send_at, "status": self.status}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ScheduleSingleSend201Response(
            send_at=payload.get("send_at"), status=payload.get("status")
        )
