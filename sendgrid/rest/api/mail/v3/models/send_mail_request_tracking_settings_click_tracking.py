from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SendMailRequestTrackingSettingsClickTracking:
    def __init__(
            self,
            enable: Optional[bool]=None,
            enable_text: Optional[bool]=None
    ):
        self.enable=enable
        self.enable_text=enable_text

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "enable": self.enable,
            "enable_text": self.enable_text
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendMailRequestTrackingSettingsClickTracking(
            enable=payload.get('enable'),
            enable_text=payload.get('enable_text')
        ) 

