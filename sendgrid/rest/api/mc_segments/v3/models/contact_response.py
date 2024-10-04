from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_segments.v3.models.contact_response_custom_fields import (
    ContactResponseCustomFields,
)


class ContactResponse:
    def __init__(
        self,
        id: Optional[str] = None,
        email: Optional[str] = None,
        phone_number_id: Optional[str] = None,
        external_id: Optional[str] = None,
        anonymous_id: Optional[str] = None,
        alternate_emails: Optional[List[str]] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        address_line_1: Optional[str] = None,
        address_line_2: Optional[str] = None,
        city: Optional[str] = None,
        state_province_region: Optional[str] = None,
        postal_code: Optional[int] = None,
        country: Optional[str] = None,
        list_ids: Optional[List[str]] = None,
        custom_fields: Optional[ContactResponseCustomFields] = None,
        segment_ids: Optional[List[str]] = None,
    ):
        self.id = id
        self.email = email
        self.phone_number_id = phone_number_id
        self.external_id = external_id
        self.anonymous_id = anonymous_id
        self.alternate_emails = alternate_emails
        self.first_name = first_name
        self.last_name = last_name
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.state_province_region = state_province_region
        self.postal_code = postal_code
        self.country = country
        self.list_ids = list_ids
        self.custom_fields = custom_fields
        self.segment_ids = segment_ids

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "email": self.email,
                "phone_number_id": self.phone_number_id,
                "external_id": self.external_id,
                "anonymous_id": self.anonymous_id,
                "alternate_emails": self.alternate_emails,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "address_line_1": self.address_line_1,
                "address_line_2": self.address_line_2,
                "city": self.city,
                "state_province_region": self.state_province_region,
                "postal_code": self.postal_code,
                "country": self.country,
                "list_ids": self.list_ids,
                "custom_fields": self.custom_fields,
                "segment_ids": self.segment_ids,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactResponse(
            id=payload.get("id"),
            email=payload.get("email"),
            phone_number_id=payload.get("phone_number_id"),
            external_id=payload.get("external_id"),
            anonymous_id=payload.get("anonymous_id"),
            alternate_emails=payload.get("alternate_emails"),
            first_name=payload.get("first_name"),
            last_name=payload.get("last_name"),
            address_line_1=payload.get("address_line_1"),
            address_line_2=payload.get("address_line_2"),
            city=payload.get("city"),
            state_province_region=payload.get("state_province_region"),
            postal_code=payload.get("postal_code"),
            country=payload.get("country"),
            list_ids=payload.get("list_ids"),
            custom_fields=payload.get("custom_fields"),
            segment_ids=payload.get("segment_ids"),
        )
