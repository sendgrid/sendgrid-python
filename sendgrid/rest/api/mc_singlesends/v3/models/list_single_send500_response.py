from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_singlesends.v3.models.list_single_send500_response_errors_inner import (
    ListSingleSend500ResponseErrorsInner,
)


class ListSingleSend500Response:
    def __init__(
        self, errors: Optional[List[ListSingleSend500ResponseErrorsInner]] = None
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
        return ListSingleSend500Response(errors=payload.get("errors"))
