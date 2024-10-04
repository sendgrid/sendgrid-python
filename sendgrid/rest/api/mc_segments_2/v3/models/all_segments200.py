from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_segments_2.v3.models.metadata import Metadata
from sendgrid.rest.api.mc_segments_2.v3.models.segment_status_response import (
    SegmentStatusResponse,
)


class AllSegments200:
    def __init__(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        contacts_count: Optional[int] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        sample_updated_at: Optional[str] = None,
        next_sample_update: Optional[str] = None,
        parent_list_ids: Optional[List[str]] = None,
        query_version: Optional[str] = None,
        metadata: Optional[Metadata] = None,
        status: Optional[SegmentStatusResponse] = None,
    ):
        self.id = id
        self.name = name
        self.contacts_count = contacts_count
        self.created_at = created_at
        self.updated_at = updated_at
        self.sample_updated_at = sample_updated_at
        self.next_sample_update = next_sample_update
        self.parent_list_ids = parent_list_ids
        self.query_version = query_version
        self.metadata = metadata
        self.status = status

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "name": self.name,
                "contacts_count": self.contacts_count,
                "created_at": self.created_at,
                "updated_at": self.updated_at,
                "sample_updated_at": self.sample_updated_at,
                "next_sample_update": self.next_sample_update,
                "parent_list_ids": self.parent_list_ids,
                "query_version": self.query_version,
                "_metadata": self.metadata,
                "status": self.status,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AllSegments200(
            id=payload.get("id"),
            name=payload.get("name"),
            contacts_count=payload.get("contacts_count"),
            created_at=payload.get("created_at"),
            updated_at=payload.get("updated_at"),
            sample_updated_at=payload.get("sample_updated_at"),
            next_sample_update=payload.get("next_sample_update"),
            parent_list_ids=payload.get("parent_list_ids"),
            query_version=payload.get("query_version"),
            metadata=payload.get("_metadata"),
            status=payload.get("status"),
        )
