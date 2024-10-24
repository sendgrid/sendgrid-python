from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ApproveScopeRequest200Response:
    def __init__(
            self,
            scope_group_name: Optional[str]=None
    ):
        self.scope_group_name=scope_group_name

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "scope_group_name": self.scope_group_name
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ApproveScopeRequest200Response(
            scope_group_name=payload.get('scope_group_name')
        ) 

