from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class MailSettingsBouncePurge:
    def __init__(
        self,
        enabled: Optional[bool] = None,
        soft_bounces: Optional[int] = None,
        hard_bounces: Optional[int] = None,
    ):
        self.enabled = enabled
        self.soft_bounces = soft_bounces
        self.hard_bounces = hard_bounces

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "enabled": self.enabled,
                "soft_bounces": self.soft_bounces,
                "hard_bounces": self.hard_bounces,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return MailSettingsBouncePurge(
            enabled=payload.get("enabled"),
            soft_bounces=payload.get("soft_bounces"),
            hard_bounces=payload.get("hard_bounces"),
        )
