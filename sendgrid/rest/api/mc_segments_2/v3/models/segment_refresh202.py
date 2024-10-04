from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SegmentRefresh202:
    def __init__(
            self,
            job_id: Optional[str]=None
    ):
        self.job_id=job_id

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "job_id": self.job_id
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SegmentRefresh202(
            job_id=payload.get('job_id')
        ) 

