from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.lmc_contactdb.v3.models.contactdb_recipient200 import (
    ContactdbRecipient200,
)


class ListRecipientsFromContactDbList200Response:
    def __init__(self, recipients: Optional[List[ContactdbRecipient200]] = None):
        self.recipients = recipients

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"recipients": self.recipients}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListRecipientsFromContactDbList200Response(
            recipients=payload.get("recipients")
        )
