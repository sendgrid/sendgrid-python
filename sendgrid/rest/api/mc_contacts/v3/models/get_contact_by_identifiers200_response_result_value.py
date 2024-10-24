from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_contacts.v3.models.contact_details3 import ContactDetails3



class GetContactByIdentifiers200ResponseResultValue:
    def __init__(
            self,
            contact: Optional[ContactDetails3]=None,
            error: Optional[str]=None
    ):
        self.contact=contact
        self.error=error

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "contact": self.contact,
            "error": self.error
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetContactByIdentifiers200ResponseResultValue(
            contact=payload.get('contact'),
            error=payload.get('error')
        ) 

