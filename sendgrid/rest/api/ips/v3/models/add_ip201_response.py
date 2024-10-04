from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.ips.v3.models.add_ip201_response_ips_inner import AddIp201ResponseIpsInner



class AddIp201Response:
    def __init__(
            self,
            ips: Optional[List[AddIp201ResponseIpsInner]]=None,
            remaining_ips: Optional[int]=None,
            warmup: Optional[bool]=None
    ):
        self.ips=ips
        self.remaining_ips=remaining_ips
        self.warmup=warmup

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "ips": self.ips,
            "remaining_ips": self.remaining_ips,
            "warmup": self.warmup
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AddIp201Response(
            ips=payload.get('ips'),
            remaining_ips=payload.get('remaining_ips'),
            warmup=payload.get('warmup')
        ) 

