from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.verified_senders.v3.models.verified_sender_response import (
    VerifiedSenderResponse,
)


class ListVerifiedSender200Response:
    def __init__(self, results: Optional[List[VerifiedSenderResponse]] = None):
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
        return ListVerifiedSender200Response(results=payload.get("results"))
