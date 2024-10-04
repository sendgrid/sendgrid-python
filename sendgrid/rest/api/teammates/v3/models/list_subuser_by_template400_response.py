from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.teammates.v3.models.list_subuser_by_template400_response_errors_inner import (
    ListSubuserByTemplate400ResponseErrorsInner,
)


class ListSubuserByTemplate400Response:
    def __init__(
        self, errors: Optional[List[ListSubuserByTemplate400ResponseErrorsInner]] = None
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
        return ListSubuserByTemplate400Response(errors=payload.get("errors"))
