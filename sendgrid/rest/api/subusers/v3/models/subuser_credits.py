from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.subusers.v3.models.reset_frequency import ResetFrequency
from sendgrid.rest.api.subusers.v3.models.type import Type


class SubuserCredits:
    def __init__(
        self,
        type: Optional[Type] = None,
        reset_frequency: Optional[ResetFrequency] = None,
        remain: Optional[int] = None,
        total: Optional[int] = None,
        used: Optional[int] = None,
    ):
        self.type = type
        self.reset_frequency = reset_frequency
        self.remain = remain
        self.total = total
        self.used = used

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "type": self.type,
                "reset_frequency": self.reset_frequency,
                "remain": self.remain,
                "total": self.total,
                "used": self.used,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SubuserCredits(
            type=payload.get("type"),
            reset_frequency=payload.get("reset_frequency"),
            remain=payload.get("remain"),
            total=payload.get("total"),
            used=payload.get("used"),
        )
