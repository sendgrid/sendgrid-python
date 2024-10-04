from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class AccountProvisioningAccountId:
    def __init__(self, account_id: Optional[str] = None):
        self.account_id = account_id

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"account_id": self.account_id}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AccountProvisioningAccountId(account_id=payload.get("account_id"))
