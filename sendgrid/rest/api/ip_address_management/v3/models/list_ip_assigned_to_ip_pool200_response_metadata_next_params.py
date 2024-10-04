from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListIpAssignedToIpPool200ResponseMetadataNextParams:
    def __init__(
        self,
        after_key: Optional[str] = None,
        limit: Optional[str] = None,
        include_region: Optional[str] = None,
    ):
        self.after_key = after_key
        self.limit = limit
        self.include_region = include_region

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "after_key": self.after_key,
                "limit": self.limit,
                "include_region": self.include_region,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListIpAssignedToIpPool200ResponseMetadataNextParams(
            after_key=payload.get("after_key"),
            limit=payload.get("limit"),
            include_region=payload.get("include_region"),
        )
