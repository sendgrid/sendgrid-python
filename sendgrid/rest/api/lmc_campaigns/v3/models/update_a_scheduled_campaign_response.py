from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class UpdateAScheduledCampaignResponse:
    def __init__(
        self,
        id: Optional[int] = None,
        send_at: Optional[int] = None,
        status: Optional[str] = None,
    ):
        self.id = id
        self.send_at = send_at
        self.status = status

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "send_at": self.send_at,
                "status": self.status,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateAScheduledCampaignResponse(
            id=payload.get("id"),
            send_at=payload.get("send_at"),
            status=payload.get("status"),
        )
