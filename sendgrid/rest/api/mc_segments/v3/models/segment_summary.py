from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SegmentSummary:
    def __init__(
            self,
            id: Optional[str]=None,
            contacts_count: Optional[int]=None,
            created_at: Optional[datetime]=None,
            name: Optional[str]=None,
            parent_list_id: Optional[str]=None,
            sample_updated_at: Optional[datetime]=None,
            updated_at: Optional[datetime]=None,
            next_sample_update: Optional[str]=None
    ):
        self.id=id
        self.contacts_count=contacts_count
        self.created_at=created_at
        self.name=name
        self.parent_list_id=parent_list_id
        self.sample_updated_at=sample_updated_at
        self.updated_at=updated_at
        self.next_sample_update=next_sample_update

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "contacts_count": self.contacts_count,
            "created_at": self.created_at,
            "name": self.name,
            "parent_list_id": self.parent_list_id,
            "sample_updated_at": self.sample_updated_at,
            "updated_at": self.updated_at,
            "next_sample_update": self.next_sample_update
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SegmentSummary(
            id=payload.get('id'),
            contacts_count=payload.get('contacts_count'),
            created_at=payload.get('created_at'),
            name=payload.get('name'),
            parent_list_id=payload.get('parent_list_id'),
            sample_updated_at=payload.get('sample_updated_at'),
            updated_at=payload.get('updated_at'),
            next_sample_update=payload.get('next_sample_update')
        ) 

