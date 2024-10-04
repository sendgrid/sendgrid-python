from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.account_provisioning.v3.models.account_provisioning_offering_v1 import (
    AccountProvisioningOfferingV1,
)
from sendgrid.rest.api.account_provisioning.v3.models.account_provisioning_profile import (
    AccountProvisioningProfile,
)


class CreateAccountParams:
    def __init__(
        self,
        profile: Optional[AccountProvisioningProfile] = None,
        offerings: Optional[List[AccountProvisioningOfferingV1]] = None,
    ):
        self.profile = profile
        self.offerings = offerings

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "profile": self.profile,
                "offerings": self.offerings,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CreateAccountParams(
            profile=payload.get("profile"), offerings=payload.get("offerings")
        )
