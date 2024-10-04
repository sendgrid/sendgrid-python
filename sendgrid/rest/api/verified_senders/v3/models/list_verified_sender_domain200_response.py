from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.verified_senders.v3.models.list_verified_sender_domain200_response_results import (
    ListVerifiedSenderDomain200ResponseResults,
)


class ListVerifiedSenderDomain200Response:
    def __init__(
        self, results: Optional[ListVerifiedSenderDomain200ResponseResults] = None
    ):
        self.results = results

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"results": self.results}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListVerifiedSenderDomain200Response(results=payload.get("results"))
