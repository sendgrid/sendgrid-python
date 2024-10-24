from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ListTrackingSetting200ResponseResultInner:
    def __init__(
            self,
            name: Optional[str]=None,
            title: Optional[str]=None,
            description: Optional[str]=None,
            enabled: Optional[bool]=None
    ):
        self.name=name
        self.title=title
        self.description=description
        self.enabled=enabled

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "name": self.name,
            "title": self.title,
            "description": self.description,
            "enabled": self.enabled
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListTrackingSetting200ResponseResultInner(
            name=payload.get('name'),
            title=payload.get('title'),
            description=payload.get('description'),
            enabled=payload.get('enabled')
        ) 

