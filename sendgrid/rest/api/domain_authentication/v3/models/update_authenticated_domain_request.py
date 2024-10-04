from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class UpdateAuthenticatedDomainRequest:
    def __init__(
        self, default: Optional[bool] = None, custom_spf: Optional[bool] = None
    ):
        self.default = default
        self.custom_spf = custom_spf

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "default": self.default,
                "custom_spf": self.custom_spf,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateAuthenticatedDomainRequest(
            default=payload.get("default"), custom_spf=payload.get("custom_spf")
        )
