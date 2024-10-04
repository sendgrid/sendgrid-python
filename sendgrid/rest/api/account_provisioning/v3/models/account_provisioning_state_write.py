from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.account_provisioning.v3.models.state1 import State1



class AccountProvisioningStateWrite:
    def __init__(
            self,
            state: Optional[State1]=None
    ):
        self.state=state

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "state": self.state
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AccountProvisioningStateWrite(
            state=payload.get('state')
        ) 

