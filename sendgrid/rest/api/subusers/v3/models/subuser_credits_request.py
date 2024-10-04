from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.subusers.v3.models.reset_frequency1 import ResetFrequency1
from sendgrid.rest.api.subusers.v3.models.type1 import Type1


class SubuserCreditsRequest:
    def __init__(
        self,
        type: Optional[Type1] = None,
        reset_frequency: Optional[ResetFrequency1] = None,
        total: Optional[int] = None,
    ):
        self.type = type
        self.reset_frequency = reset_frequency
        self.total = total

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "type": self.type,
                "reset_frequency": self.reset_frequency,
                "total": self.total,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SubuserCreditsRequest(
            type=payload.get("type"),
            reset_frequency=payload.get("reset_frequency"),
            total=payload.get("total"),
        )
