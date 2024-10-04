from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.ip_address_management.v3.models.get_ip_pool200_response_ip_count_by_region_inner import (
    GetIpPool200ResponseIpCountByRegionInner,
)


class GetIpPool200Response:
    def __init__(
        self,
        name: Optional[str] = None,
        id: Optional[str] = None,
        ips_preview: Optional[List[str]] = None,
        total_ip_count: Optional[int] = None,
        ip_count_by_region: Optional[
            List[GetIpPool200ResponseIpCountByRegionInner]
        ] = None,
    ):
        self.name = name
        self.id = id
        self.ips_preview = ips_preview
        self.total_ip_count = total_ip_count
        self.ip_count_by_region = ip_count_by_region

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "name": self.name,
                "id": self.id,
                "ips_preview": self.ips_preview,
                "total_ip_count": self.total_ip_count,
                "ip_count_by_region": self.ip_count_by_region,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetIpPool200Response(
            name=payload.get("name"),
            id=payload.get("id"),
            ips_preview=payload.get("ips_preview"),
            total_ip_count=payload.get("total_ip_count"),
            ip_count_by_region=payload.get("ip_count_by_region"),
        )
