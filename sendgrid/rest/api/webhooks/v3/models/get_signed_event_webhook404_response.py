from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.webhooks.v3.models.get_signed_event_webhook404_response_errors_inner import (
    GetSignedEventWebhook404ResponseErrorsInner,
)


class GetSignedEventWebhook404Response:
    def __init__(
        self, errors: Optional[List[GetSignedEventWebhook404ResponseErrorsInner]] = None
    ):
        self.errors = errors

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"errors": self.errors}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetSignedEventWebhook404Response(errors=payload.get("errors"))
