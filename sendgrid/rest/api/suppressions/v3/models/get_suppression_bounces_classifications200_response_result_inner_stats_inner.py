from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class GetSuppressionBouncesClassifications200ResponseResultInnerStatsInner:
    def __init__(
            self,
            domain: Optional[str]=None,
            count: Optional[int]=None
    ):
        self.domain=domain
        self.count=count

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "domain": self.domain,
            "count": self.count
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetSuppressionBouncesClassifications200ResponseResultInnerStatsInner(
            domain=payload.get('domain'),
            count=payload.get('count')
        ) 

