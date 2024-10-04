from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.sso.v3.models.permission_type import PermissionType


class SsoTeammatesBaseRequestPropsSubuserAccessInner:
    def __init__(
        self,
        id: Optional[int] = None,
        permission_type: Optional[PermissionType] = None,
        scopes: Optional[List[str]] = None,
    ):
        self.id = id
        self.permission_type = permission_type
        self.scopes = scopes

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "permission_type": self.permission_type,
                "scopes": self.scopes,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SsoTeammatesBaseRequestPropsSubuserAccessInner(
            id=payload.get("id"),
            permission_type=payload.get("permission_type"),
            scopes=payload.get("scopes"),
        )
