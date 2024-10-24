from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_singlesends.v3.models.editor import Editor



class SinglesendRequestEmailConfig:
    def __init__(
            self,
            subject: Optional[str]=None,
            html_content: Optional[str]=None,
            plain_content: Optional[str]=None,
            generate_plain_content: Optional[bool]=None,
            design_id: Optional[str]=None,
            editor: Optional[Editor]=None,
            suppression_group_id: Optional[int]=None,
            custom_unsubscribe_url: Optional[str]=None,
            sender_id: Optional[int]=None,
            ip_pool: Optional[str]=None
    ):
        self.subject=subject
        self.html_content=html_content
        self.plain_content=plain_content
        self.generate_plain_content=generate_plain_content
        self.design_id=design_id
        self.editor=editor
        self.suppression_group_id=suppression_group_id
        self.custom_unsubscribe_url=custom_unsubscribe_url
        self.sender_id=sender_id
        self.ip_pool=ip_pool

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "subject": self.subject,
            "html_content": self.html_content,
            "plain_content": self.plain_content,
            "generate_plain_content": self.generate_plain_content,
            "design_id": self.design_id,
            "editor": self.editor,
            "suppression_group_id": self.suppression_group_id,
            "custom_unsubscribe_url": self.custom_unsubscribe_url,
            "sender_id": self.sender_id,
            "ip_pool": self.ip_pool
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SinglesendRequestEmailConfig(
            subject=payload.get('subject'),
            html_content=payload.get('html_content'),
            plain_content=payload.get('plain_content'),
            generate_plain_content=payload.get('generate_plain_content'),
            design_id=payload.get('design_id'),
            editor=payload.get('editor'),
            suppression_group_id=payload.get('suppression_group_id'),
            custom_unsubscribe_url=payload.get('custom_unsubscribe_url'),
            sender_id=payload.get('sender_id'),
            ip_pool=payload.get('ip_pool')
        ) 

