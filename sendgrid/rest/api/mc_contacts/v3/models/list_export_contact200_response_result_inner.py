from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_contacts.v3.models.list_export_contact200_response_result_inner_metadata import ListExportContact200ResponseResultInnerMetadata
from sendgrid.rest.api.mc_contacts.v3.models.list_export_contact200_response_result_inner_segments_inner import ListExportContact200ResponseResultInnerSegmentsInner



class ListExportContact200ResponseResultInner:
    def __init__(
            self,
            id: Optional[str]=None,
            status: Optional[str]=None,
            created_at: Optional[str]=None,
            completed_at: Optional[str]=None,
            expires_at: Optional[str]=None,
            urls: Optional[List[str]]=None,
            user_id: Optional[str]=None,
            export_type: Optional[str]=None,
            segments: Optional[List[ListExportContact200ResponseResultInnerSegmentsInner]]=None,
            lists: Optional[List[ListExportContact200ResponseResultInnerSegmentsInner]]=None,
            metadata: Optional[ListExportContact200ResponseResultInnerMetadata]=None
    ):
        self.id=id
        self.status=status
        self.created_at=created_at
        self.completed_at=completed_at
        self.expires_at=expires_at
        self.urls=urls
        self.user_id=user_id
        self.export_type=export_type
        self.segments=segments
        self.lists=lists
        self.metadata=metadata

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "status": self.status,
            "created_at": self.created_at,
            "completed_at": self.completed_at,
            "expires_at": self.expires_at,
            "urls": self.urls,
            "user_id": self.user_id,
            "export_type": self.export_type,
            "segments": self.segments,
            "lists": self.lists,
            "_metadata": self.metadata
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListExportContact200ResponseResultInner(
            id=payload.get('id'),
            status=payload.get('status'),
            created_at=payload.get('created_at'),
            completed_at=payload.get('completed_at'),
            expires_at=payload.get('expires_at'),
            urls=payload.get('urls'),
            user_id=payload.get('user_id'),
            export_type=payload.get('export_type'),
            segments=payload.get('segments'),
            lists=payload.get('lists'),
            metadata=payload.get('_metadata')
        ) 

