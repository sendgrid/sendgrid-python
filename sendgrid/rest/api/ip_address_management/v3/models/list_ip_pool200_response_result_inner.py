from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.ip_address_management.v3.models.items import Items


class ListIpPool200ResponseResultInner:
    def __init__(
        self,
        name: Optional[str] = None,
        id: Optional[str] = None,
        regions: Optional[List[Items]] = None,
        ips_preview: Optional[List[str]] = None,
        total_ip_count: Optional[int] = None,
    ):
        self.name = name
        self.id = id
        self.regions = regions
        self.ips_preview = ips_preview
        self.total_ip_count = total_ip_count

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "name": self.name,
                "id": self.id,
                "regions": self.regions,
                "ips_preview": self.ips_preview,
                "total_ip_count": self.total_ip_count,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListIpPool200ResponseResultInner(
            name=payload.get("name"),
            id=payload.get("id"),
            regions=payload.get("regions"),
            ips_preview=payload.get("ips_preview"),
            total_ip_count=payload.get("total_ip_count"),
        )
