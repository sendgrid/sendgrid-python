from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class MailSettingsFooter:
    def __init__(
            self,
            enabled: Optional[bool]=None,
            html_content: Optional[str]=None,
            plain_content: Optional[str]=None
    ):
        self.enabled=enabled
        self.html_content=html_content
        self.plain_content=plain_content

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "enabled": self.enabled,
            "html_content": self.html_content,
            "plain_content": self.plain_content
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return MailSettingsFooter(
            enabled=payload.get('enabled'),
            html_content=payload.get('html_content'),
            plain_content=payload.get('plain_content')
        ) 

