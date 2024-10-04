from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListVerifiedSenderDomain200ResponseResults:
    def __init__(
        self,
        soft_failures: Optional[List[str]] = None,
        hard_failures: Optional[List[str]] = None,
    ):
        self.soft_failures = soft_failures
        self.hard_failures = hard_failures

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "soft_failures": self.soft_failures,
                "hard_failures": self.hard_failures,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListVerifiedSenderDomain200ResponseResults(
            soft_failures=payload.get("soft_failures"),
            hard_failures=payload.get("hard_failures"),
        )
