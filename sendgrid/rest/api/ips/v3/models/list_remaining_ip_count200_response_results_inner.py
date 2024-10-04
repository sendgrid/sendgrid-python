from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ListRemainingIpCount200ResponseResultsInner:
    def __init__(
            self,
            remaining: Optional[int]=None,
            period: Optional[str]=None,
            price_per_ip: Optional[float]=None
    ):
        self.remaining=remaining
        self.period=period
        self.price_per_ip=price_per_ip

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "remaining": self.remaining,
            "period": self.period,
            "price_per_ip": self.price_per_ip
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListRemainingIpCount200ResponseResultsInner(
            remaining=payload.get('remaining'),
            period=payload.get('period'),
            price_per_ip=payload.get('price_per_ip')
        ) 

