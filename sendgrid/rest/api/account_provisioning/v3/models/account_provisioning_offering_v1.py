from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.account_provisioning.v3.models.type import Type



class AccountProvisioningOfferingV1:
    def __init__(
            self,
            name: Optional[str]=None,
            type: Optional[Type]=None,
            quantity: Optional[int]=None
    ):
        self.name=name
        self.type=type
        self.quantity=quantity

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "name": self.name,
            "type": self.type,
            "quantity": self.quantity
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AccountProvisioningOfferingV1(
            name=payload.get('name'),
            type=payload.get('type'),
            quantity=payload.get('quantity')
        ) 

