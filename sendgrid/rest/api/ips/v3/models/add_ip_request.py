from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class AddIpRequest:
    def __init__(
        self,
        count: Optional[int] = None,
        subusers: Optional[List[str]] = None,
        warmup: Optional[bool] = None,
    ):
        self.count = count
        self.subusers = subusers
        self.warmup = warmup

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "count": self.count,
                "subusers": self.subusers,
                "warmup": self.warmup,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AddIpRequest(
            count=payload.get("count"),
            subusers=payload.get("subusers"),
            warmup=payload.get("warmup"),
        )
