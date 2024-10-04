from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ClickTracking:
    def __init__(
            self,
            enable_text: Optional[bool]=None,
            enabled: Optional[bool]=None
    ):
        self.enable_text=enable_text
        self.enabled=enabled

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "enable_text": self.enable_text,
            "enabled": self.enabled
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ClickTracking(
            enable_text=payload.get('enable_text'),
            enabled=payload.get('enabled')
        ) 

