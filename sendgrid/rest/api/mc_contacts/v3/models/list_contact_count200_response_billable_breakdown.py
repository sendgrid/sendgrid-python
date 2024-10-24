from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ListContactCount200ResponseBillableBreakdown:
    def __init__(
            self,
            total: Optional[int]=None,
            breakdown: Optional[object]=None
    ):
        self.total=total
        self.breakdown=breakdown

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "total": self.total,
            "breakdown": self.breakdown
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListContactCount200ResponseBillableBreakdown(
            total=payload.get('total'),
            breakdown=payload.get('breakdown')
        ) 

