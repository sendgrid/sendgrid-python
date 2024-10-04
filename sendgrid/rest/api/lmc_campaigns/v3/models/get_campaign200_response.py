from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class GetCampaign200Response:
    def __init__(
        self,
        categories: Optional[List[str]] = None,
        custom_unsubscribe_url: Optional[str] = None,
        html_content: Optional[str] = None,
        id: Optional[int] = None,
        ip_pool: Optional[str] = None,
        list_ids: Optional[List[int]] = None,
        plain_content: Optional[str] = None,
        segment_ids: Optional[List[int]] = None,
        sender_id: Optional[int] = None,
        status: Optional[str] = None,
        subject: Optional[str] = None,
        suppression_group_id: Optional[int] = None,
        title: Optional[str] = None,
    ):
        self.categories = categories
        self.custom_unsubscribe_url = custom_unsubscribe_url
        self.html_content = html_content
        self.id = id
        self.ip_pool = ip_pool
        self.list_ids = list_ids
        self.plain_content = plain_content
        self.segment_ids = segment_ids
        self.sender_id = sender_id
        self.status = status
        self.subject = subject
        self.suppression_group_id = suppression_group_id
        self.title = title

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "categories": self.categories,
                "custom_unsubscribe_url": self.custom_unsubscribe_url,
                "html_content": self.html_content,
                "id": self.id,
                "ip_pool": self.ip_pool,
                "list_ids": self.list_ids,
                "plain_content": self.plain_content,
                "segment_ids": self.segment_ids,
                "sender_id": self.sender_id,
                "status": self.status,
                "subject": self.subject,
                "suppression_group_id": self.suppression_group_id,
                "title": self.title,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetCampaign200Response(
            categories=payload.get("categories"),
            custom_unsubscribe_url=payload.get("custom_unsubscribe_url"),
            html_content=payload.get("html_content"),
            id=payload.get("id"),
            ip_pool=payload.get("ip_pool"),
            list_ids=payload.get("list_ids"),
            plain_content=payload.get("plain_content"),
            segment_ids=payload.get("segment_ids"),
            sender_id=payload.get("sender_id"),
            status=payload.get("status"),
            subject=payload.get("subject"),
            suppression_group_id=payload.get("suppression_group_id"),
            title=payload.get("title"),
        )
