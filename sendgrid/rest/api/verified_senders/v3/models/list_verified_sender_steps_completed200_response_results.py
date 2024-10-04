from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListVerifiedSenderStepsCompleted200ResponseResults:
    def __init__(
        self,
        sender_verified: Optional[bool] = None,
        domain_verified: Optional[bool] = None,
    ):
        self.sender_verified = sender_verified
        self.domain_verified = domain_verified

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "sender_verified": self.sender_verified,
                "domain_verified": self.domain_verified,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListVerifiedSenderStepsCompleted200ResponseResults(
            sender_verified=payload.get("sender_verified"),
            domain_verified=payload.get("domain_verified"),
        )
