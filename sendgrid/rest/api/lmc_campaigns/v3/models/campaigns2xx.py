from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.lmc_campaigns.v3.models.editor import Editor


class Campaigns2xx:
    def __init__(
        self,
        title: Optional[str] = None,
        subject: Optional[str] = None,
        sender_id: Optional[int] = None,
        list_ids: Optional[List[int]] = None,
        segment_ids: Optional[List[int]] = None,
        categories: Optional[List[str]] = None,
        suppression_group_id: Optional[int] = None,
        custom_unsubscribe_url: Optional[str] = None,
        ip_pool: Optional[str] = None,
        html_content: Optional[str] = None,
        plain_content: Optional[str] = None,
        editor: Optional[Editor] = None,
        status: Optional[str] = None,
        id: Optional[int] = None,
    ):
        self.title = title
        self.subject = subject
        self.sender_id = sender_id
        self.list_ids = list_ids
        self.segment_ids = segment_ids
        self.categories = categories
        self.suppression_group_id = suppression_group_id
        self.custom_unsubscribe_url = custom_unsubscribe_url
        self.ip_pool = ip_pool
        self.html_content = html_content
        self.plain_content = plain_content
        self.editor = editor
        self.status = status
        self.id = id

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "title": self.title,
                "subject": self.subject,
                "sender_id": self.sender_id,
                "list_ids": self.list_ids,
                "segment_ids": self.segment_ids,
                "categories": self.categories,
                "suppression_group_id": self.suppression_group_id,
                "custom_unsubscribe_url": self.custom_unsubscribe_url,
                "ip_pool": self.ip_pool,
                "html_content": self.html_content,
                "plain_content": self.plain_content,
                "editor": self.editor,
                "status": self.status,
                "id": self.id,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return Campaigns2xx(
            title=payload.get("title"),
            subject=payload.get("subject"),
            sender_id=payload.get("sender_id"),
            list_ids=payload.get("list_ids"),
            segment_ids=payload.get("segment_ids"),
            categories=payload.get("categories"),
            suppression_group_id=payload.get("suppression_group_id"),
            custom_unsubscribe_url=payload.get("custom_unsubscribe_url"),
            ip_pool=payload.get("ip_pool"),
            html_content=payload.get("html_content"),
            plain_content=payload.get("plain_content"),
            editor=payload.get("editor"),
            status=payload.get("status"),
            id=payload.get("id"),
        )
