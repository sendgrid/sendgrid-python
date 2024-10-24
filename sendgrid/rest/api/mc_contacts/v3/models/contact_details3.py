from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_contacts.v3.models.self_metadata import SelfMetadata



class ContactDetails3:
    def __init__(
            self,
            id: Optional[str]=None,
            first_name: Optional[str]=None,
            last_name: Optional[str]=None,
            unique_name: Optional[str]=None,
            email: Optional[str]=None,
            phone_number_id: Optional[str]=None,
            external_id: Optional[str]=None,
            anonymous_id: Optional[str]=None,
            alternate_emails: Optional[List[str]]=None,
            address_line_1: Optional[str]=None,
            address_line_2: Optional[str]=None,
            city: Optional[str]=None,
            state_province_region: Optional[str]=None,
            country: Optional[str]=None,
            postal_code: Optional[str]=None,
            phone_number: Optional[str]=None,
            whatsapp: Optional[str]=None,
            line: Optional[str]=None,
            facebook: Optional[str]=None,
            list_ids: Optional[List[str]]=None,
            segment_ids: Optional[List[str]]=None,
            custom_fields: Optional[object]=None,
            created_at: Optional[str]=None,
            updated_at: Optional[str]=None,
            metadata: Optional[SelfMetadata]=None
    ):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.unique_name=unique_name
        self.email=email
        self.phone_number_id=phone_number_id
        self.external_id=external_id
        self.anonymous_id=anonymous_id
        self.alternate_emails=alternate_emails
        self.address_line_1=address_line_1
        self.address_line_2=address_line_2
        self.city=city
        self.state_province_region=state_province_region
        self.country=country
        self.postal_code=postal_code
        self.phone_number=phone_number
        self.whatsapp=whatsapp
        self.line=line
        self.facebook=facebook
        self.list_ids=list_ids
        self.segment_ids=segment_ids
        self.custom_fields=custom_fields
        self.created_at=created_at
        self.updated_at=updated_at
        self.metadata=metadata

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "unique_name": self.unique_name,
            "email": self.email,
            "phone_number_id": self.phone_number_id,
            "external_id": self.external_id,
            "anonymous_id": self.anonymous_id,
            "alternate_emails": self.alternate_emails,
            "address_line_1": self.address_line_1,
            "address_line_2": self.address_line_2,
            "city": self.city,
            "state_province_region": self.state_province_region,
            "country": self.country,
            "postal_code": self.postal_code,
            "phone_number": self.phone_number,
            "whatsapp": self.whatsapp,
            "line": self.line,
            "facebook": self.facebook,
            "list_ids": self.list_ids,
            "segment_ids": self.segment_ids,
            "custom_fields": self.custom_fields,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "_metadata": self.metadata
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactDetails3(
            id=payload.get('id'),
            first_name=payload.get('first_name'),
            last_name=payload.get('last_name'),
            unique_name=payload.get('unique_name'),
            email=payload.get('email'),
            phone_number_id=payload.get('phone_number_id'),
            external_id=payload.get('external_id'),
            anonymous_id=payload.get('anonymous_id'),
            alternate_emails=payload.get('alternate_emails'),
            address_line_1=payload.get('address_line_1'),
            address_line_2=payload.get('address_line_2'),
            city=payload.get('city'),
            state_province_region=payload.get('state_province_region'),
            country=payload.get('country'),
            postal_code=payload.get('postal_code'),
            phone_number=payload.get('phone_number'),
            whatsapp=payload.get('whatsapp'),
            line=payload.get('line'),
            facebook=payload.get('facebook'),
            list_ids=payload.get('list_ids'),
            segment_ids=payload.get('segment_ids'),
            custom_fields=payload.get('custom_fields'),
            created_at=payload.get('created_at'),
            updated_at=payload.get('updated_at'),
            metadata=payload.get('_metadata')
        ) 

