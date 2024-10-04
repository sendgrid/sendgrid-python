from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.lmc_contactdb.v3.models.list_status200_response_status_inner import (
    ListStatus200ResponseStatusInner,
)


class ListStatus200Response:
    def __init__(self, status: Optional[List[ListStatus200ResponseStatusInner]] = None):
        self.status = status

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"status": self.status}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListStatus200Response(status=payload.get("status"))
