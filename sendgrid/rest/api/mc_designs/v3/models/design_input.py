from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_designs.v3.models.editor import Editor



class DesignInput:
    def __init__(
            self,
            name: Optional[str]=None,
            editor: Optional[Editor]=None,
            html_content: Optional[str]=None,
            plain_content: Optional[str]=None
    ):
        self.name=name
        self.editor=editor
        self.html_content=html_content
        self.plain_content=plain_content

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "name": self.name,
            "editor": self.editor,
            "html_content": self.html_content,
            "plain_content": self.plain_content
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return DesignInput(
            name=payload.get('name'),
            editor=payload.get('editor'),
            html_content=payload.get('html_content'),
            plain_content=payload.get('plain_content')
        ) 

