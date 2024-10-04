from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.ip_address_management.v3.models.list_ip200_response_result_inner_pools_inner import (
    ListIp200ResponseResultInnerPoolsInner,
)
from sendgrid.rest.api.ip_address_management.v3.models.region import Region


class ListIp200ResponseResultInner:
    def __init__(
        self,
        ip: Optional[str] = None,
        pools: Optional[List[ListIp200ResponseResultInnerPoolsInner]] = None,
        is_auto_warmup: Optional[bool] = None,
        is_parent_assigned: Optional[bool] = None,
        updated_at: Optional[int] = None,
        is_enabled: Optional[bool] = None,
        is_leased: Optional[bool] = None,
        added_at: Optional[int] = None,
        region: Optional[Region] = None,
    ):
        self.ip = ip
        self.pools = pools
        self.is_auto_warmup = is_auto_warmup
        self.is_parent_assigned = is_parent_assigned
        self.updated_at = updated_at
        self.is_enabled = is_enabled
        self.is_leased = is_leased
        self.added_at = added_at
        self.region = region

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "ip": self.ip,
                "pools": self.pools,
                "is_auto_warmup": self.is_auto_warmup,
                "is_parent_assigned": self.is_parent_assigned,
                "updated_at": self.updated_at,
                "is_enabled": self.is_enabled,
                "is_leased": self.is_leased,
                "added_at": self.added_at,
                "region": self.region,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListIp200ResponseResultInner(
            ip=payload.get("ip"),
            pools=payload.get("pools"),
            is_auto_warmup=payload.get("is_auto_warmup"),
            is_parent_assigned=payload.get("is_parent_assigned"),
            updated_at=payload.get("updated_at"),
            is_enabled=payload.get("is_enabled"),
            is_leased=payload.get("is_leased"),
            added_at=payload.get("added_at"),
            region=payload.get("region"),
        )
