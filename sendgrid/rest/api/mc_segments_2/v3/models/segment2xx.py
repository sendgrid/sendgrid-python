from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_segments_2.v3.models.contact_response import ContactResponse
from sendgrid.rest.api.mc_segments_2.v3.models.segment_status_response import (
    SegmentStatusResponse,
)


class Segment2xx:
    def __init__(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        query_dsl: Optional[str] = None,
        contacts_count: Optional[int] = None,
        contacts_sample: Optional[List[ContactResponse]] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        sample_updated_at: Optional[str] = None,
        next_sample_update: Optional[str] = None,
        parent_list_ids: Optional[List[str]] = None,
        query_version: Optional[str] = None,
        status: Optional[SegmentStatusResponse] = None,
        refreshes_used: Optional[int] = None,
        max_refreshes: Optional[int] = None,
        last_refreshed_at: Optional[str] = None,
    ):
        self.id = id
        self.name = name
        self.query_dsl = query_dsl
        self.contacts_count = contacts_count
        self.contacts_sample = contacts_sample
        self.created_at = created_at
        self.updated_at = updated_at
        self.sample_updated_at = sample_updated_at
        self.next_sample_update = next_sample_update
        self.parent_list_ids = parent_list_ids
        self.query_version = query_version
        self.status = status
        self.refreshes_used = refreshes_used
        self.max_refreshes = max_refreshes
        self.last_refreshed_at = last_refreshed_at

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "name": self.name,
                "query_dsl": self.query_dsl,
                "contacts_count": self.contacts_count,
                "contacts_sample": self.contacts_sample,
                "created_at": self.created_at,
                "updated_at": self.updated_at,
                "sample_updated_at": self.sample_updated_at,
                "next_sample_update": self.next_sample_update,
                "parent_list_ids": self.parent_list_ids,
                "query_version": self.query_version,
                "status": self.status,
                "refreshes_used": self.refreshes_used,
                "max_refreshes": self.max_refreshes,
                "last_refreshed_at": self.last_refreshed_at,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return Segment2xx(
            id=payload.get("id"),
            name=payload.get("name"),
            query_dsl=payload.get("query_dsl"),
            contacts_count=payload.get("contacts_count"),
            contacts_sample=payload.get("contacts_sample"),
            created_at=payload.get("created_at"),
            updated_at=payload.get("updated_at"),
            sample_updated_at=payload.get("sample_updated_at"),
            next_sample_update=payload.get("next_sample_update"),
            parent_list_ids=payload.get("parent_list_ids"),
            query_version=payload.get("query_version"),
            status=payload.get("status"),
            refreshes_used=payload.get("refreshes_used"),
            max_refreshes=payload.get("max_refreshes"),
            last_refreshed_at=payload.get("last_refreshed_at"),
        )
