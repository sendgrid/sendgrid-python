from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.email_validation.v3.models.status import Status



class GetValidationsEmailJobs200ResponseResultInner:
    def __init__(
            self,
            id: Optional[str]=None,
            status: Optional[Status]=None,
            started_at: Optional[float]=None,
            finished_at: Optional[float]=None
    ):
        self.id=id
        self.status=status
        self.started_at=started_at
        self.finished_at=finished_at

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "status": self.status,
            "started_at": self.started_at,
            "finished_at": self.finished_at
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetValidationsEmailJobs200ResponseResultInner(
            id=payload.get('id'),
            status=payload.get('status'),
            started_at=payload.get('started_at'),
            finished_at=payload.get('finished_at')
        ) 

