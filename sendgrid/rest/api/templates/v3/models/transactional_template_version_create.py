from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.templates.v3.models.active import Active
from sendgrid.rest.api.templates.v3.models.editor import Editor



class TransactionalTemplateVersionCreate:
    def __init__(
            self,
            active: Optional[Active]=None,
            name: Optional[str]=None,
            html_content: Optional[str]=None,
            plain_content: Optional[str]=None,
            generate_plain_content: Optional[bool]=None,
            subject: Optional[str]=None,
            editor: Optional[Editor]=None,
            test_data: Optional[str]=None
    ):
        self.active=active
        self.name=name
        self.html_content=html_content
        self.plain_content=plain_content
        self.generate_plain_content=generate_plain_content
        self.subject=subject
        self.editor=editor
        self.test_data=test_data

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "active": self.active,
            "name": self.name,
            "html_content": self.html_content,
            "plain_content": self.plain_content,
            "generate_plain_content": self.generate_plain_content,
            "subject": self.subject,
            "editor": self.editor,
            "test_data": self.test_data
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return TransactionalTemplateVersionCreate(
            active=payload.get('active'),
            name=payload.get('name'),
            html_content=payload.get('html_content'),
            plain_content=payload.get('plain_content'),
            generate_plain_content=payload.get('generate_plain_content'),
            subject=payload.get('subject'),
            editor=payload.get('editor'),
            test_data=payload.get('test_data')
        ) 

