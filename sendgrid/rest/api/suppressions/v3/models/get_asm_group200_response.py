from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class GetAsmGroup200Response:
    def __init__(
            self,
            name: Optional[str]=None,
            description: Optional[str]=None,
            is_default: Optional[bool]=None,
            id: Optional[int]=None,
            unsubscribes: Optional[int]=None,
            last_email_sent_at: Optional[str]=None
    ):
        self.name=name
        self.description=description
        self.is_default=is_default
        self.id=id
        self.unsubscribes=unsubscribes
        self.last_email_sent_at=last_email_sent_at

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "name": self.name,
            "description": self.description,
            "is_default": self.is_default,
            "id": self.id,
            "unsubscribes": self.unsubscribes,
            "last_email_sent_at": self.last_email_sent_at
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetAsmGroup200Response(
            name=payload.get('name'),
            description=payload.get('description'),
            is_default=payload.get('is_default'),
            id=payload.get('id'),
            unsubscribes=payload.get('unsubscribes'),
            last_email_sent_at=payload.get('last_email_sent_at')
        ) 

