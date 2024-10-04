from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class AccountProvisioningAccount:
    def __init__(self, id: Optional[str] = None, created_at: Optional[datetime] = None):
        self.id = id
        self.created_at = created_at

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"id": self.id, "created_at": self.created_at}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AccountProvisioningAccount(
            id=payload.get("id"), created_at=payload.get("created_at")
        )
