from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_designs.v3.models.editor import Editor



class DesignCommonProperties:
    def __init__(
            self,
            name: Optional[str]=None,
            editor: Optional[Editor]=None,
            generate_plain_content: Optional[bool]=None,
            subject: Optional[str]=None,
            categories: Optional[List[str]]=None
    ):
        self.name=name
        self.editor=editor
        self.generate_plain_content=generate_plain_content
        self.subject=subject
        self.categories=categories

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "name": self.name,
            "editor": self.editor,
            "generate_plain_content": self.generate_plain_content,
            "subject": self.subject,
            "categories": self.categories
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return DesignCommonProperties(
            name=payload.get('name'),
            editor=payload.get('editor'),
            generate_plain_content=payload.get('generate_plain_content'),
            subject=payload.get('subject'),
            categories=payload.get('categories')
        ) 

