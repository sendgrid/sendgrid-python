from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SegmentRefreshRequest:
    def __init__(
            self,
            user_time_zone: Optional[str]=None
    ):
        self.user_time_zone=user_time_zone

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "user_time_zone": self.user_time_zone
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SegmentRefreshRequest(
            user_time_zone=payload.get('user_time_zone')
        ) 

