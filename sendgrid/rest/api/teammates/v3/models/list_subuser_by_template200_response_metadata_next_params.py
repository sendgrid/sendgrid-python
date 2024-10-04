from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListSubuserByTemplate200ResponseMetadataNextParams:
    def __init__(
        self,
        limit: Optional[int] = None,
        after_subuser_id: Optional[int] = None,
        username: Optional[str] = None,
    ):
        self.limit = limit
        self.after_subuser_id = after_subuser_id
        self.username = username

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "limit": self.limit,
                "after_subuser_id": self.after_subuser_id,
                "username": self.username,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListSubuserByTemplate200ResponseMetadataNextParams(
            limit=payload.get("limit"),
            after_subuser_id=payload.get("after_subuser_id"),
            username=payload.get("username"),
        )
