from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.scheduled_sends.v3.models.status import Status



class CancelOrPauseAScheduledSendRequest:
    def __init__(
            self,
            batch_id: Optional[str]=None,
            status: Optional[Status]=None
    ):
        self.batch_id=batch_id
        self.status=status

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "batch_id": self.batch_id,
            "status": self.status
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CancelOrPauseAScheduledSendRequest(
            batch_id=payload.get('batch_id'),
            status=payload.get('status')
        ) 

