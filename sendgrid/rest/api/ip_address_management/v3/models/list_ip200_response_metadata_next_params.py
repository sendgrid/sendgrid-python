from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.ip_address_management.v3.models.region1 import Region1


class ListIp200ResponseMetadataNextParams:
    def __init__(
        self,
        after_key: Optional[str] = None,
        before_key: Optional[str] = None,
        ip: Optional[str] = None,
        is_leased: Optional[bool] = None,
        is_enabled: Optional[bool] = None,
        is_parent_assigned: Optional[bool] = None,
        pool: Optional[str] = None,
        start_added_at: Optional[str] = None,
        end_added_at: Optional[str] = None,
        limit: Optional[str] = None,
        region: Optional[Region1] = None,
        include_region: Optional[str] = None,
    ):
        self.after_key = after_key
        self.before_key = before_key
        self.ip = ip
        self.is_leased = is_leased
        self.is_enabled = is_enabled
        self.is_parent_assigned = is_parent_assigned
        self.pool = pool
        self.start_added_at = start_added_at
        self.end_added_at = end_added_at
        self.limit = limit
        self.region = region
        self.include_region = include_region

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "after_key": self.after_key,
                "before_key": self.before_key,
                "ip": self.ip,
                "is_leased": self.is_leased,
                "is_enabled": self.is_enabled,
                "is_parent_assigned": self.is_parent_assigned,
                "pool": self.pool,
                "start_added_at": self.start_added_at,
                "end_added_at": self.end_added_at,
                "limit": self.limit,
                "region": self.region,
                "include_region": self.include_region,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListIp200ResponseMetadataNextParams(
            after_key=payload.get("after_key"),
            before_key=payload.get("before_key"),
            ip=payload.get("ip"),
            is_leased=payload.get("is_leased"),
            is_enabled=payload.get("is_enabled"),
            is_parent_assigned=payload.get("is_parent_assigned"),
            pool=payload.get("pool"),
            start_added_at=payload.get("start_added_at"),
            end_added_at=payload.get("end_added_at"),
            limit=payload.get("limit"),
            region=payload.get("region"),
            include_region=payload.get("include_region"),
        )
