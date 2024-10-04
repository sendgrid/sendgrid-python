from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.lmc_contactdb.v3.models.contactdb_recipient_response201_errors_inner import ContactdbRecipientResponse201ErrorsInner



class ContactdbRecipientResponse201:
    def __init__(
            self,
            error_count: Optional[float]=None,
            error_indices: Optional[List[float]]=None,
            new_count: Optional[float]=None,
            persisted_recipients: Optional[List[str]]=None,
            updated_count: Optional[float]=None,
            errors: Optional[List[ContactdbRecipientResponse201ErrorsInner]]=None
    ):
        self.error_count=error_count
        self.error_indices=error_indices
        self.new_count=new_count
        self.persisted_recipients=persisted_recipients
        self.updated_count=updated_count
        self.errors=errors

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "error_count": self.error_count,
            "error_indices": self.error_indices,
            "new_count": self.new_count,
            "persisted_recipients": self.persisted_recipients,
            "updated_count": self.updated_count,
            "errors": self.errors
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactdbRecipientResponse201(
            error_count=payload.get('error_count'),
            error_indices=payload.get('error_indices'),
            new_count=payload.get('new_count'),
            persisted_recipients=payload.get('persisted_recipients'),
            updated_count=payload.get('updated_count'),
            errors=payload.get('errors')
        ) 

