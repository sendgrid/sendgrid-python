from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class UpdateDesignRequest:
    def __init__(
        self,
        name: Optional[str] = None,
        html_content: Optional[str] = None,
        plain_content: Optional[str] = None,
        generate_plain_content: Optional[bool] = None,
        subject: Optional[str] = None,
        categories: Optional[List[str]] = None,
    ):
        self.name = name
        self.html_content = html_content
        self.plain_content = plain_content
        self.generate_plain_content = generate_plain_content
        self.subject = subject
        self.categories = categories

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "name": self.name,
                "html_content": self.html_content,
                "plain_content": self.plain_content,
                "generate_plain_content": self.generate_plain_content,
                "subject": self.subject,
                "categories": self.categories,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateDesignRequest(
            name=payload.get("name"),
            html_content=payload.get("html_content"),
            plain_content=payload.get("plain_content"),
            generate_plain_content=payload.get("generate_plain_content"),
            subject=payload.get("subject"),
            categories=payload.get("categories"),
        )
