from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class AutmoationsLinkStatsResponseResultsInner:
    def __init__(
            self,
            url: Optional[str]=None,
            url_location: Optional[int]=None,
            step_id: Optional[str]=None,
            clicks: Optional[int]=None
    ):
        self.url=url
        self.url_location=url_location
        self.step_id=step_id
        self.clicks=clicks

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "url": self.url,
            "url_location": self.url_location,
            "step_id": self.step_id,
            "clicks": self.clicks
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AutmoationsLinkStatsResponseResultsInner(
            url=payload.get('url'),
            url_location=payload.get('url_location'),
            step_id=payload.get('step_id'),
            clicks=payload.get('clicks')
        ) 

