from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.teammates.v3.models.user_type import UserType



class ListTeammate200ResponseResultInner:
    def __init__(
            self,
            username: Optional[str]=None,
            email: Optional[str]=None,
            first_name: Optional[str]=None,
            last_name: Optional[str]=None,
            user_type: Optional[UserType]=None,
            is_admin: Optional[bool]=None,
            phone: Optional[str]=None,
            website: Optional[str]=None,
            address: Optional[str]=None,
            address2: Optional[str]=None,
            city: Optional[str]=None,
            state: Optional[str]=None,
            zip: Optional[str]=None,
            country: Optional[str]=None
    ):
        self.username=username
        self.email=email
        self.first_name=first_name
        self.last_name=last_name
        self.user_type=user_type
        self.is_admin=is_admin
        self.phone=phone
        self.website=website
        self.address=address
        self.address2=address2
        self.city=city
        self.state=state
        self.zip=zip
        self.country=country

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "user_type": self.user_type,
            "is_admin": self.is_admin,
            "phone": self.phone,
            "website": self.website,
            "address": self.address,
            "address2": self.address2,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
            "country": self.country
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListTeammate200ResponseResultInner(
            username=payload.get('username'),
            email=payload.get('email'),
            first_name=payload.get('first_name'),
            last_name=payload.get('last_name'),
            user_type=payload.get('user_type'),
            is_admin=payload.get('is_admin'),
            phone=payload.get('phone'),
            website=payload.get('website'),
            address=payload.get('address'),
            address2=payload.get('address2'),
            city=payload.get('city'),
            state=payload.get('state'),
            zip=payload.get('zip'),
            country=payload.get('country')
        ) 

