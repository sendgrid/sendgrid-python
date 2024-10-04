from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class UpdateIpRequest:
    def __init__(
        self,
        is_auto_warmup: Optional[bool] = None,
        is_parent_assigned: Optional[bool] = None,
        is_enabled: Optional[bool] = None,
    ):
        self.is_auto_warmup = is_auto_warmup
        self.is_parent_assigned = is_parent_assigned
        self.is_enabled = is_enabled

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "is_auto_warmup": self.is_auto_warmup,
                "is_parent_assigned": self.is_parent_assigned,
                "is_enabled": self.is_enabled,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateIpRequest(
            is_auto_warmup=payload.get("is_auto_warmup"),
            is_parent_assigned=payload.get("is_parent_assigned"),
            is_enabled=payload.get("is_enabled"),
        )
