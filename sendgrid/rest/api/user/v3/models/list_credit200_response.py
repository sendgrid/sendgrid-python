from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ListCredit200Response:
    def __init__(
            self,
            remain: Optional[int]=None,
            total: Optional[int]=None,
            overage: Optional[int]=None,
            used: Optional[int]=None,
            last_reset: Optional[str]=None,
            next_reset: Optional[str]=None,
            reset_frequency: Optional[str]=None
    ):
        self.remain=remain
        self.total=total
        self.overage=overage
        self.used=used
        self.last_reset=last_reset
        self.next_reset=next_reset
        self.reset_frequency=reset_frequency

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "remain": self.remain,
            "total": self.total,
            "overage": self.overage,
            "used": self.used,
            "last_reset": self.last_reset,
            "next_reset": self.next_reset,
            "reset_frequency": self.reset_frequency
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListCredit200Response(
            remain=payload.get('remain'),
            total=payload.get('total'),
            overage=payload.get('overage'),
            used=payload.get('used'),
            last_reset=payload.get('last_reset'),
            next_reset=payload.get('next_reset'),
            reset_frequency=payload.get('reset_frequency')
        ) 

