from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.subusers.v3.models.region3 import Region3
from sendgrid.rest.api.subusers.v3.models.subuser_post_credit_allocation import (
    SubuserPostCreditAllocation,
)


class SubuserPost:
    def __init__(
        self,
        username: Optional[str] = None,
        user_id: Optional[float] = None,
        email: Optional[str] = None,
        credit_allocation: Optional[SubuserPostCreditAllocation] = None,
        region: Optional[Region3] = None,
    ):
        self.username = username
        self.user_id = user_id
        self.email = email
        self.credit_allocation = credit_allocation
        self.region = region

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "username": self.username,
                "user_id": self.user_id,
                "email": self.email,
                "credit_allocation": self.credit_allocation,
                "region": self.region,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SubuserPost(
            username=payload.get("username"),
            user_id=payload.get("user_id"),
            email=payload.get("email"),
            credit_allocation=payload.get("credit_allocation"),
            region=payload.get("region"),
        )
