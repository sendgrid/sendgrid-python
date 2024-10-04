from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class UpdateAsmGroupRequest:
    def __init__(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        is_default: Optional[bool] = None,
    ):
        self.name = name
        self.description = description
        self.is_default = is_default

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "name": self.name,
                "description": self.description,
                "is_default": self.is_default,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateAsmGroupRequest(
            name=payload.get("name"),
            description=payload.get("description"),
            is_default=payload.get("is_default"),
        )
