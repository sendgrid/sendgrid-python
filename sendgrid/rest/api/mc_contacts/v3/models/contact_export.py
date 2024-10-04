from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_contacts.v3.models.metadata import Metadata
from sendgrid.rest.api.mc_contacts.v3.models.status import Status



class ContactExport:
    def __init__(
            self,
            id: Optional[str]=None,
            status: Optional[Status]=None,
            created_at: Optional[str]=None,
            updated_at: Optional[str]=None,
            completed_at: Optional[str]=None,
            expires_at: Optional[str]=None,
            urls: Optional[List[str]]=None,
            message: Optional[str]=None,
            metadata: Optional[Metadata]=None,
            contact_count: Optional[int]=None
    ):
        self.id=id
        self.status=status
        self.created_at=created_at
        self.updated_at=updated_at
        self.completed_at=completed_at
        self.expires_at=expires_at
        self.urls=urls
        self.message=message
        self.metadata=metadata
        self.contact_count=contact_count

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "completed_at": self.completed_at,
            "expires_at": self.expires_at,
            "urls": self.urls,
            "message": self.message,
            "_metadata": self.metadata,
            "contact_count": self.contact_count
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactExport(
            id=payload.get('id'),
            status=payload.get('status'),
            created_at=payload.get('created_at'),
            updated_at=payload.get('updated_at'),
            completed_at=payload.get('completed_at'),
            expires_at=payload.get('expires_at'),
            urls=payload.get('urls'),
            message=payload.get('message'),
            metadata=payload.get('_metadata'),
            contact_count=payload.get('contact_count')
        ) 

