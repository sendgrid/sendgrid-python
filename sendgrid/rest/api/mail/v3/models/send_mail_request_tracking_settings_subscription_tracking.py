from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SendMailRequestTrackingSettingsSubscriptionTracking:
    def __init__(
            self,
            enable: Optional[bool]=None,
            text: Optional[str]=None,
            html: Optional[str]=None,
            substitution_tag: Optional[str]=None
    ):
        self.enable=enable
        self.text=text
        self.html=html
        self.substitution_tag=substitution_tag

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "enable": self.enable,
            "text": self.text,
            "html": self.html,
            "substitution_tag": self.substitution_tag
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendMailRequestTrackingSettingsSubscriptionTracking(
            enable=payload.get('enable'),
            text=payload.get('text'),
            html=payload.get('html'),
            substitution_tag=payload.get('substitution_tag')
        ) 

