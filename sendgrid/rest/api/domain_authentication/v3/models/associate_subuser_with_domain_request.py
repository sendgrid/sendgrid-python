from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class AssociateSubuserWithDomainRequest:
    def __init__(self, username: Optional[str] = None):
        self.username = username

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"username": self.username}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AssociateSubuserWithDomainRequest(username=payload.get("username"))
