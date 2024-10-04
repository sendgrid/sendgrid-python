from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.scopes.v3.models.list_scope401_response_errors_inner import ListScope401ResponseErrorsInner



class ListScope401Response:
    def __init__(
            self,
            errors: Optional[List[ListScope401ResponseErrorsInner]]=None
    ):
        self.errors=errors

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "errors": self.errors
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListScope401Response(
            errors=payload.get('errors')
        ) 

