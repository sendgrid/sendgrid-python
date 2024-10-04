from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.lmc_contactdb.v3.models.search_recipient200_response_recipients_inner_custom_fields_inner import (
    SearchRecipient200ResponseRecipientsInnerCustomFieldsInner,
)


class SearchRecipient200ResponseRecipientsInner:
    def __init__(
        self,
        created_at: Optional[int] = None,
        email: Optional[str] = None,
        id: Optional[str] = None,
        last_emailed: Optional[int] = None,
        last_clicked: Optional[int] = None,
        last_opened: Optional[int] = None,
        custom_fields: Optional[
            List[SearchRecipient200ResponseRecipientsInnerCustomFieldsInner]
        ] = None,
        updated_at: Optional[int] = None,
        first_name: Optional[str] = None,
    ):
        self.created_at = created_at
        self.email = email
        self.id = id
        self.last_emailed = last_emailed
        self.last_clicked = last_clicked
        self.last_opened = last_opened
        self.custom_fields = custom_fields
        self.updated_at = updated_at
        self.first_name = first_name

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "created_at": self.created_at,
                "email": self.email,
                "id": self.id,
                "last_emailed": self.last_emailed,
                "last_clicked": self.last_clicked,
                "last_opened": self.last_opened,
                "custom_fields": self.custom_fields,
                "updated_at": self.updated_at,
                "first_name": self.first_name,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SearchRecipient200ResponseRecipientsInner(
            created_at=payload.get("created_at"),
            email=payload.get("email"),
            id=payload.get("id"),
            last_emailed=payload.get("last_emailed"),
            last_clicked=payload.get("last_clicked"),
            last_opened=payload.get("last_opened"),
            custom_fields=payload.get("custom_fields"),
            updated_at=payload.get("updated_at"),
            first_name=payload.get("first_name"),
        )
