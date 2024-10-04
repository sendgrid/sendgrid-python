from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class UpdateACampaignRequest:
    def __init__(
            self,
            title: Optional[str]=None,
            subject: Optional[str]=None,
            categories: Optional[List[str]]=None,
            html_content: Optional[str]=None,
            plain_content: Optional[str]=None
    ):
        self.title=title
        self.subject=subject
        self.categories=categories
        self.html_content=html_content
        self.plain_content=plain_content

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "title": self.title,
            "subject": self.subject,
            "categories": self.categories,
            "html_content": self.html_content,
            "plain_content": self.plain_content
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateACampaignRequest(
            title=payload.get('title'),
            subject=payload.get('subject'),
            categories=payload.get('categories'),
            html_content=payload.get('html_content'),
            plain_content=payload.get('plain_content')
        ) 

