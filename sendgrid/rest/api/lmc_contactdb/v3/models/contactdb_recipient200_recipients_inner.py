from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.lmc_contactdb.v3.models.contactdb_custom_field_id_value import ContactdbCustomFieldIdValue



class ContactdbRecipient200RecipientsInner:
    def __init__(
            self,
            id: Optional[str]=None,
            created_at: Optional[float]=None,
            custom_fields: Optional[List[ContactdbCustomFieldIdValue]]=None,
            email: Optional[str]=None,
            first_name: Optional[str]=None,
            last_name: Optional[str]=None,
            last_clicked: Optional[float]=None,
            last_emailed: Optional[float]=None,
            last_opened: Optional[float]=None,
            updated_at: Optional[float]=None
    ):
        self.id=id
        self.created_at=created_at
        self.custom_fields=custom_fields
        self.email=email
        self.first_name=first_name
        self.last_name=last_name
        self.last_clicked=last_clicked
        self.last_emailed=last_emailed
        self.last_opened=last_opened
        self.updated_at=updated_at

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "created_at": self.created_at,
            "custom_fields": self.custom_fields,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "last_clicked": self.last_clicked,
            "last_emailed": self.last_emailed,
            "last_opened": self.last_opened,
            "updated_at": self.updated_at
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactdbRecipient200RecipientsInner(
            id=payload.get('id'),
            created_at=payload.get('created_at'),
            custom_fields=payload.get('custom_fields'),
            email=payload.get('email'),
            first_name=payload.get('first_name'),
            last_name=payload.get('last_name'),
            last_clicked=payload.get('last_clicked'),
            last_emailed=payload.get('last_emailed'),
            last_opened=payload.get('last_opened'),
            updated_at=payload.get('updated_at')
        ) 

