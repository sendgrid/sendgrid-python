from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.ip_address_management.v3.models.region2 import Region2


class AddIp201Response:
    def __init__(
        self,
        ip: Optional[str] = None,
        is_auto_warmup: Optional[bool] = None,
        is_parent_assigned: Optional[bool] = None,
        subusers: Optional[List[str]] = None,
        region: Optional[Region2] = None,
    ):
        self.ip = ip
        self.is_auto_warmup = is_auto_warmup
        self.is_parent_assigned = is_parent_assigned
        self.subusers = subusers
        self.region = region

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "ip": self.ip,
                "is_auto_warmup": self.is_auto_warmup,
                "is_parent_assigned": self.is_parent_assigned,
                "subusers": self.subusers,
                "region": self.region,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AddIp201Response(
            ip=payload.get("ip"),
            is_auto_warmup=payload.get("is_auto_warmup"),
            is_parent_assigned=payload.get("is_parent_assigned"),
            subusers=payload.get("subusers"),
            region=payload.get("region"),
        )
