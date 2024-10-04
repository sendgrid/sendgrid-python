from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListPartnerSetting200ResponseResultInner:
    def __init__(
        self,
        title: Optional[str] = None,
        enabled: Optional[bool] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ):
        self.title = title
        self.enabled = enabled
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "title": self.title,
                "enabled": self.enabled,
                "name": self.name,
                "description": self.description,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListPartnerSetting200ResponseResultInner(
            title=payload.get("title"),
            enabled=payload.get("enabled"),
            name=payload.get("name"),
            description=payload.get("description"),
        )
