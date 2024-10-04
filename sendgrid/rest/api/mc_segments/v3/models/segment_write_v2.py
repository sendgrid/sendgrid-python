from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class SegmentWriteV2:
    def __init__(
        self,
        name: Optional[str] = None,
        parent_list_ids: Optional[List[str]] = None,
        query_dsl: Optional[str] = None,
    ):
        self.name = name
        self.parent_list_ids = parent_list_ids
        self.query_dsl = query_dsl

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "name": self.name,
                "parent_list_ids": self.parent_list_ids,
                "query_dsl": self.query_dsl,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SegmentWriteV2(
            name=payload.get("name"),
            parent_list_ids=payload.get("parent_list_ids"),
            query_dsl=payload.get("query_dsl"),
        )
