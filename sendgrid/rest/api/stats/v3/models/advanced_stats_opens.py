from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class AdvancedStatsOpens:
    def __init__(self, opens: Optional[int] = None, unique_opens: Optional[int] = None):
        self.opens = opens
        self.unique_opens = unique_opens

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "opens": self.opens,
                "unique_opens": self.unique_opens,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AdvancedStatsOpens(
            opens=payload.get("opens"), unique_opens=payload.get("unique_opens")
        )
