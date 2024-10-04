from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SendMailRequestTrackingSettingsGanalytics:
    def __init__(
            self,
            enable: Optional[bool]=None,
            utm_source: Optional[str]=None,
            utm_medium: Optional[str]=None,
            utm_term: Optional[str]=None,
            utm_content: Optional[str]=None,
            utm_campaign: Optional[str]=None
    ):
        self.enable=enable
        self.utm_source=utm_source
        self.utm_medium=utm_medium
        self.utm_term=utm_term
        self.utm_content=utm_content
        self.utm_campaign=utm_campaign

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "enable": self.enable,
            "utm_source": self.utm_source,
            "utm_medium": self.utm_medium,
            "utm_term": self.utm_term,
            "utm_content": self.utm_content,
            "utm_campaign": self.utm_campaign
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendMailRequestTrackingSettingsGanalytics(
            enable=payload.get('enable'),
            utm_source=payload.get('utm_source'),
            utm_medium=payload.get('utm_medium'),
            utm_term=payload.get('utm_term'),
            utm_content=payload.get('utm_content'),
            utm_campaign=payload.get('utm_campaign')
        ) 

