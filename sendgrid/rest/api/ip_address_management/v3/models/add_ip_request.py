from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.ip_address_management.v3.models.region3 import Region3



class AddIpRequest:
    def __init__(
            self,
            is_auto_warmup: Optional[bool]=None,
            is_parent_assigned: Optional[bool]=None,
            subusers: Optional[List[str]]=None,
            region: Optional[Region3]=None,
            include_region: Optional[bool]=None
    ):
        self.is_auto_warmup=is_auto_warmup
        self.is_parent_assigned=is_parent_assigned
        self.subusers=subusers
        self.region=region
        self.include_region=include_region

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "is_auto_warmup": self.is_auto_warmup,
            "is_parent_assigned": self.is_parent_assigned,
            "subusers": self.subusers,
            "region": self.region,
            "include_region": self.include_region
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AddIpRequest(
            is_auto_warmup=payload.get('is_auto_warmup'),
            is_parent_assigned=payload.get('is_parent_assigned'),
            subusers=payload.get('subusers'),
            region=payload.get('region'),
            include_region=payload.get('include_region')
        ) 

