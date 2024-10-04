from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.ip_address_management.v3.models.get_ip200_response_pools_inner import GetIp200ResponsePoolsInner



class GetIp200Response:
    def __init__(
            self,
            ip: Optional[str]=None,
            is_parent_assigned: Optional[bool]=None,
            is_auto_warmup: Optional[bool]=None,
            pools: Optional[List[GetIp200ResponsePoolsInner]]=None,
            added_at: Optional[int]=None,
            updated_at: Optional[int]=None,
            is_enabled: Optional[bool]=None,
            is_leased: Optional[bool]=None,
            region: Optional[str]=None
    ):
        self.ip=ip
        self.is_parent_assigned=is_parent_assigned
        self.is_auto_warmup=is_auto_warmup
        self.pools=pools
        self.added_at=added_at
        self.updated_at=updated_at
        self.is_enabled=is_enabled
        self.is_leased=is_leased
        self.region=region

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "ip": self.ip,
            "is_parent_assigned": self.is_parent_assigned,
            "is_auto_warmup": self.is_auto_warmup,
            "pools": self.pools,
            "added_at": self.added_at,
            "updated_at": self.updated_at,
            "is_enabled": self.is_enabled,
            "is_leased": self.is_leased,
            "region": self.region
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetIp200Response(
            ip=payload.get('ip'),
            is_parent_assigned=payload.get('is_parent_assigned'),
            is_auto_warmup=payload.get('is_auto_warmup'),
            pools=payload.get('pools'),
            added_at=payload.get('added_at'),
            updated_at=payload.get('updated_at'),
            is_enabled=payload.get('is_enabled'),
            is_leased=payload.get('is_leased'),
            region=payload.get('region')
        ) 

