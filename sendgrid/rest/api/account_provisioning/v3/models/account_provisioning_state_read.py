from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.account_provisioning.v3.models.state import State


class AccountProvisioningStateRead:
    def __init__(self, state: Optional[State] = None):
        self.state = state

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"state": self.state}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AccountProvisioningStateRead(state=payload.get("state"))
