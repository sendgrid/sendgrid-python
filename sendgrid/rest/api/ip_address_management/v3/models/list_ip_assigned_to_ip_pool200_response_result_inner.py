from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.ip_address_management.v3.models.list_ip200_response_result_inner_pools_inner import (
    ListIp200ResponseResultInnerPoolsInner,
)
from sendgrid.rest.api.ip_address_management.v3.models.region6 import Region6


class ListIpAssignedToIpPool200ResponseResultInner:
    def __init__(
        self,
        ip: Optional[str] = None,
        region: Optional[Region6] = None,
        pools: Optional[List[ListIp200ResponseResultInnerPoolsInner]] = None,
    ):
        self.ip = ip
        self.region = region
        self.pools = pools

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "ip": self.ip,
                "region": self.region,
                "pools": self.pools,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListIpAssignedToIpPool200ResponseResultInner(
            ip=payload.get("ip"),
            region=payload.get("region"),
            pools=payload.get("pools"),
        )
