from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class InvalidEmail:
    def __init__(
            self,
            created: Optional[int]=None,
            email: Optional[str]=None,
            reason: Optional[str]=None
    ):
        self.created=created
        self.email=email
        self.reason=reason

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "created": self.created,
            "email": self.email,
            "reason": self.reason
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return InvalidEmail(
            created=payload.get('created'),
            email=payload.get('email'),
            reason=payload.get('reason')
        ) 

