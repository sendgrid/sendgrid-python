from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class SendTestMarketingEmailRequest:
    def __init__(
        self,
        template_id: Optional[str] = None,
        version_id_override: Optional[str] = None,
        sender_id: Optional[int] = None,
        custom_unsubscribe_url: Optional[str] = None,
        suppression_group_id: Optional[int] = None,
        emails: Optional[List[str]] = None,
        from_address: Optional[str] = None,
    ):
        self.template_id = template_id
        self.version_id_override = version_id_override
        self.sender_id = sender_id
        self.custom_unsubscribe_url = custom_unsubscribe_url
        self.suppression_group_id = suppression_group_id
        self.emails = emails
        self.from_address = from_address

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "template_id": self.template_id,
                "version_id_override": self.version_id_override,
                "sender_id": self.sender_id,
                "custom_unsubscribe_url": self.custom_unsubscribe_url,
                "suppression_group_id": self.suppression_group_id,
                "emails": self.emails,
                "from_address": self.from_address,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendTestMarketingEmailRequest(
            template_id=payload.get("template_id"),
            version_id_override=payload.get("version_id_override"),
            sender_id=payload.get("sender_id"),
            custom_unsubscribe_url=payload.get("custom_unsubscribe_url"),
            suppression_group_id=payload.get("suppression_group_id"),
            emails=payload.get("emails"),
            from_address=payload.get("from_address"),
        )
