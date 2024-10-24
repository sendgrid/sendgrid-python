from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class MailSettingsForwardBounce:
    def __init__(
            self,
            email: Optional[str]=None,
            enabled: Optional[bool]=None
    ):
        self.email=email
        self.enabled=enabled

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "email": self.email,
            "enabled": self.enabled
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return MailSettingsForwardBounce(
            email=payload.get('email'),
            enabled=payload.get('enabled')
        ) 
