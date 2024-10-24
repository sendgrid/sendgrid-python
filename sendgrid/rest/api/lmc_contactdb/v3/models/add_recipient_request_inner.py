from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class AddRecipientRequestInner:
    def __init__(
            self,
            email: Optional[str]=None,
            first_name: Optional[str]=None,
            last_name: Optional[str]=None,
            age: Optional[int]=None
    ):
        self.email=email
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AddRecipientRequestInner(
            email=payload.get('email'),
            first_name=payload.get('first_name'),
            last_name=payload.get('last_name'),
            age=payload.get('age')
        ) 

