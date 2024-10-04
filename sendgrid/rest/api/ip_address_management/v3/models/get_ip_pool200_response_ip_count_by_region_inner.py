from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.ip_address_management.v3.models.region5 import Region5


class GetIpPool200ResponseIpCountByRegionInner:
    def __init__(self, region: Optional[Region5] = None, count: Optional[int] = None):
        self.region = region
        self.count = count

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"region": self.region, "count": self.count}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetIpPool200ResponseIpCountByRegionInner(
            region=payload.get("region"), count=payload.get("count")
        )
