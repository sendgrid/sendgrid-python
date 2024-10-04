from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.ip_address_management.v3.models.region4 import Region4



class ListIpPool200ResponseMetadataNextParams:
    def __init__(
            self,
            after_key: Optional[str]=None,
            ip: Optional[str]=None,
            limit: Optional[str]=None,
            region: Optional[Region4]=None,
            include_region: Optional[str]=None
    ):
        self.after_key=after_key
        self.ip=ip
        self.limit=limit
        self.region=region
        self.include_region=include_region

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "after_key": self.after_key,
            "ip": self.ip,
            "limit": self.limit,
            "region": self.region,
            "include_region": self.include_region
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListIpPool200ResponseMetadataNextParams(
            after_key=payload.get('after_key'),
            ip=payload.get('ip'),
            limit=payload.get('limit'),
            region=payload.get('region'),
            include_region=payload.get('include_region')
        ) 

