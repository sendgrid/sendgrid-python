from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_designs.v3.models.editor import Editor


class DesignDuplicateInput:
    def __init__(self, name: Optional[str] = None, editor: Optional[Editor] = None):
        self.name = name
        self.editor = editor

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"name": self.name, "editor": self.editor}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return DesignDuplicateInput(
            name=payload.get("name"), editor=payload.get("editor")
        )
