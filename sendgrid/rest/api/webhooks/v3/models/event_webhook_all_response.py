from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.webhooks.v3.models.event_webhook_signed_response import EventWebhookSignedResponse



class EventWebhookAllResponse:
    def __init__(
            self,
            max_allowed: Optional[float]=None,
            webhooks: Optional[List[EventWebhookSignedResponse]]=None
    ):
        self.max_allowed=max_allowed
        self.webhooks=webhooks

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "max_allowed": self.max_allowed,
            "webhooks": self.webhooks
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return EventWebhookAllResponse(
            max_allowed=payload.get('max_allowed'),
            webhooks=payload.get('webhooks')
        ) 

