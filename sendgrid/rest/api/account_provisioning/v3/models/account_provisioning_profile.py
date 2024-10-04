from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class AccountProvisioningProfile:
    def __init__(
            self,
            first_name: Optional[str]=None,
            last_name: Optional[str]=None,
            company_name: Optional[str]=None,
            company_website: Optional[str]=None,
            email: Optional[str]=None,
            phone: Optional[str]=None,
            timezone: Optional[str]=None
    ):
        self.first_name=first_name
        self.last_name=last_name
        self.company_name=company_name
        self.company_website=company_website
        self.email=email
        self.phone=phone
        self.timezone=timezone

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "company_name": self.company_name,
            "company_website": self.company_website,
            "email": self.email,
            "phone": self.phone,
            "timezone": self.timezone
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AccountProvisioningProfile(
            first_name=payload.get('first_name'),
            last_name=payload.get('last_name'),
            company_name=payload.get('company_name'),
            company_website=payload.get('company_website'),
            email=payload.get('email'),
            phone=payload.get('phone'),
            timezone=payload.get('timezone')
        ) 

