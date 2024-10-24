from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.lmc_campaigns.v3.models.status import Status



class ScheduleACampaignResponse:
    def __init__(
            self,
            id: Optional[int]=None,
            send_at: Optional[int]=None,
            status: Optional[Status]=None
    ):
        self.id=id
        self.send_at=send_at
        self.status=status

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "send_at": self.send_at,
            "status": self.status
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ScheduleACampaignResponse(
            id=payload.get('id'),
            send_at=payload.get('send_at'),
            status=payload.get('status')
        ) 

