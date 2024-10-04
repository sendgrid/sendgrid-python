from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_contacts.v3.models.contact_request_custom_fields import ContactRequestCustomFields



class ContactRequest:
    def __init__(
            self,
            address_line_1: Optional[str]=None,
            address_line_2: Optional[str]=None,
            alternate_emails: Optional[List[str]]=None,
            city: Optional[str]=None,
            country: Optional[str]=None,
            email: Optional[str]=None,
            phone_number_id: Optional[str]=None,
            external_id: Optional[str]=None,
            anonymous_id: Optional[str]=None,
            first_name: Optional[str]=None,
            last_name: Optional[str]=None,
            postal_code: Optional[str]=None,
            state_province_region: Optional[str]=None,
            custom_fields: Optional[ContactRequestCustomFields]=None
    ):
        self.address_line_1=address_line_1
        self.address_line_2=address_line_2
        self.alternate_emails=alternate_emails
        self.city=city
        self.country=country
        self.email=email
        self.phone_number_id=phone_number_id
        self.external_id=external_id
        self.anonymous_id=anonymous_id
        self.first_name=first_name
        self.last_name=last_name
        self.postal_code=postal_code
        self.state_province_region=state_province_region
        self.custom_fields=custom_fields

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "address_line_1": self.address_line_1,
            "address_line_2": self.address_line_2,
            "alternate_emails": self.alternate_emails,
            "city": self.city,
            "country": self.country,
            "email": self.email,
            "phone_number_id": self.phone_number_id,
            "external_id": self.external_id,
            "anonymous_id": self.anonymous_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "postal_code": self.postal_code,
            "state_province_region": self.state_province_region,
            "custom_fields": self.custom_fields
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactRequest(
            address_line_1=payload.get('address_line_1'),
            address_line_2=payload.get('address_line_2'),
            alternate_emails=payload.get('alternate_emails'),
            city=payload.get('city'),
            country=payload.get('country'),
            email=payload.get('email'),
            phone_number_id=payload.get('phone_number_id'),
            external_id=payload.get('external_id'),
            anonymous_id=payload.get('anonymous_id'),
            first_name=payload.get('first_name'),
            last_name=payload.get('last_name'),
            postal_code=payload.get('postal_code'),
            state_province_region=payload.get('state_province_region'),
            custom_fields=payload.get('custom_fields')
        ) 

