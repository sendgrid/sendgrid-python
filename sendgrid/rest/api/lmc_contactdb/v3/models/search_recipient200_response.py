from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.lmc_contactdb.v3.models.search_recipient200_response_recipients_inner import (
    SearchRecipient200ResponseRecipientsInner,
)


class SearchRecipient200Response:
    def __init__(
        self,
        recipients: Optional[List[SearchRecipient200ResponseRecipientsInner]] = None,
        recipient_count: Optional[int] = None,
    ):
        self.recipients = recipients
        self.recipient_count = recipient_count

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "recipients": self.recipients,
                "recipient_count": self.recipient_count,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SearchRecipient200Response(
            recipients=payload.get("recipients"),
            recipient_count=payload.get("recipient_count"),
        )
