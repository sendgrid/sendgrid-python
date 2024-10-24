from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ViewScheduledTimeOfACampaignResponse:
    def __init__(
            self,
            send_at: Optional[int]=None
    ):
        self.send_at=send_at

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "send_at": self.send_at
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ViewScheduledTimeOfACampaignResponse(
            send_at=payload.get('send_at')
        ) 

