from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.teammates.v3.models.list_subuser_by_template200_response_metadata import (
    ListSubuserByTemplate200ResponseMetadata,
)
from sendgrid.rest.api.teammates.v3.models.list_subuser_by_template200_response_subuser_access_inner import (
    ListSubuserByTemplate200ResponseSubuserAccessInner,
)


class ListSubuserByTemplate200Response:
    def __init__(
        self,
        has_restricted_subuser_access: Optional[bool] = None,
        subuser_access: Optional[
            List[ListSubuserByTemplate200ResponseSubuserAccessInner]
        ] = None,
        metadata: Optional[ListSubuserByTemplate200ResponseMetadata] = None,
    ):
        self.has_restricted_subuser_access = has_restricted_subuser_access
        self.subuser_access = subuser_access
        self.metadata = metadata

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "has_restricted_subuser_access": self.has_restricted_subuser_access,
                "subuser_access": self.subuser_access,
                "_metadata": self.metadata,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListSubuserByTemplate200Response(
            has_restricted_subuser_access=payload.get("has_restricted_subuser_access"),
            subuser_access=payload.get("subuser_access"),
            metadata=payload.get("_metadata"),
        )
