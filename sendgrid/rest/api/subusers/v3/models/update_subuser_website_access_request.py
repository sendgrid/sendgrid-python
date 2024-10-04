from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class UpdateSubuserWebsiteAccessRequest:
    def __init__(self, disabled: Optional[bool] = None):
        self.disabled = disabled

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"disabled": self.disabled}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateSubuserWebsiteAccessRequest(disabled=payload.get("disabled"))
