from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListReputation200ResponseInner:
    def __init__(
        self, reputation: Optional[float] = None, username: Optional[str] = None
    ):
        self.reputation = reputation
        self.username = username

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "reputation": self.reputation,
                "username": self.username,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListReputation200ResponseInner(
            reputation=payload.get("reputation"), username=payload.get("username")
        )
