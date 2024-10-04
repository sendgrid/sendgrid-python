from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.teammates.v3.models.permission_type import PermissionType


class ListSubuserByTemplate200ResponseSubuserAccessInner:
    def __init__(
        self,
        id: Optional[int] = None,
        username: Optional[str] = None,
        email: Optional[str] = None,
        disabled: Optional[bool] = None,
        permission_type: Optional[PermissionType] = None,
        scopes: Optional[List[str]] = None,
    ):
        self.id = id
        self.username = username
        self.email = email
        self.disabled = disabled
        self.permission_type = permission_type
        self.scopes = scopes

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "username": self.username,
                "email": self.email,
                "disabled": self.disabled,
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
        return ListSubuserByTemplate200ResponseSubuserAccessInner(
            id=payload.get("id"),
            username=payload.get("username"),
            email=payload.get("email"),
            disabled=payload.get("disabled"),
            permission_type=payload.get("permission_type"),
            scopes=payload.get("scopes"),
        )
