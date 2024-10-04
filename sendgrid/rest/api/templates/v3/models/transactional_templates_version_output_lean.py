from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.templates.v3.models.active1 import Active1
from sendgrid.rest.api.templates.v3.models.editor1 import Editor1


class TransactionalTemplatesVersionOutputLean:
    def __init__(
        self,
        id: Optional[str] = None,
        template_id: Optional[str] = None,
        active: Optional[Active1] = None,
        name: Optional[str] = None,
        subject: Optional[str] = None,
        updated_at: Optional[str] = None,
        generate_plain_content: Optional[bool] = None,
        html_content: Optional[str] = None,
        plain_content: Optional[str] = None,
        editor: Optional[Editor1] = None,
        thumbnail_url: Optional[str] = None,
    ):
        self.id = id
        self.template_id = template_id
        self.active = active
        self.name = name
        self.subject = subject
        self.updated_at = updated_at
        self.generate_plain_content = generate_plain_content
        self.html_content = html_content
        self.plain_content = plain_content
        self.editor = editor
        self.thumbnail_url = thumbnail_url

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "template_id": self.template_id,
                "active": self.active,
                "name": self.name,
                "subject": self.subject,
                "updated_at": self.updated_at,
                "generate_plain_content": self.generate_plain_content,
                "html_content": self.html_content,
                "plain_content": self.plain_content,
                "editor": self.editor,
                "thumbnail_url": self.thumbnail_url,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return TransactionalTemplatesVersionOutputLean(
            id=payload.get("id"),
            template_id=payload.get("template_id"),
            active=payload.get("active"),
            name=payload.get("name"),
            subject=payload.get("subject"),
            updated_at=payload.get("updated_at"),
            generate_plain_content=payload.get("generate_plain_content"),
            html_content=payload.get("html_content"),
            plain_content=payload.get("plain_content"),
            editor=payload.get("editor"),
            thumbnail_url=payload.get("thumbnail_url"),
        )
