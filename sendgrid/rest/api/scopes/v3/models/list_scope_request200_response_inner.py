from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListScopeRequest200ResponseInner:
    def __init__(
        self,
        id: Optional[int] = None,
        scope_group_name: Optional[str] = None,
        username: Optional[str] = None,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
    ):
        self.id = id
        self.scope_group_name = scope_group_name
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "scope_group_name": self.scope_group_name,
                "username": self.username,
                "email": self.email,
                "first_name": self.first_name,
                "last_name": self.last_name,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListScopeRequest200ResponseInner(
            id=payload.get("id"),
            scope_group_name=payload.get("scope_group_name"),
            username=payload.get("username"),
            email=payload.get("email"),
            first_name=payload.get("first_name"),
            last_name=payload.get("last_name"),
        )
