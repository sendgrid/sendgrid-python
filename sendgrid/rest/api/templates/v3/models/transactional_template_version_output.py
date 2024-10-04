from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.templates.v3.models.active1 import Active1
from sendgrid.rest.api.templates.v3.models.editor1 import Editor1
from sendgrid.rest.api.templates.v3.models.transactional_template_warning import TransactionalTemplateWarning



class TransactionalTemplateVersionOutput:
    def __init__(
            self,
            warnings: Optional[List[TransactionalTemplateWarning]]=None,
            active: Optional[Active1]=None,
            name: Optional[str]=None,
            html_content: Optional[str]=None,
            plain_content: Optional[str]=None,
            generate_plain_content: Optional[bool]=None,
            subject: Optional[str]=None,
            editor: Optional[Editor1]=None,
            test_data: Optional[str]=None,
            id: Optional[str]=None,
            template_id: Optional[str]=None,
            updated_at: Optional[str]=None,
            thumbnail_url: Optional[str]=None
    ):
        self.warnings=warnings
        self.active=active
        self.name=name
        self.html_content=html_content
        self.plain_content=plain_content
        self.generate_plain_content=generate_plain_content
        self.subject=subject
        self.editor=editor
        self.test_data=test_data
        self.id=id
        self.template_id=template_id
        self.updated_at=updated_at
        self.thumbnail_url=thumbnail_url

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "warnings": self.warnings,
            "active": self.active,
            "name": self.name,
            "html_content": self.html_content,
            "plain_content": self.plain_content,
            "generate_plain_content": self.generate_plain_content,
            "subject": self.subject,
            "editor": self.editor,
            "test_data": self.test_data,
            "id": self.id,
            "template_id": self.template_id,
            "updated_at": self.updated_at,
            "thumbnail_url": self.thumbnail_url
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return TransactionalTemplateVersionOutput(
            warnings=payload.get('warnings'),
            active=payload.get('active'),
            name=payload.get('name'),
            html_content=payload.get('html_content'),
            plain_content=payload.get('plain_content'),
            generate_plain_content=payload.get('generate_plain_content'),
            subject=payload.get('subject'),
            editor=payload.get('editor'),
            test_data=payload.get('test_data'),
            id=payload.get('id'),
            template_id=payload.get('template_id'),
            updated_at=payload.get('updated_at'),
            thumbnail_url=payload.get('thumbnail_url')
        ) 

