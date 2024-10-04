from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListParseStatic200ResponseInnerStatsInnerMetrics:
    def __init__(self, received: Optional[float] = None):
        self.received = received

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"received": self.received}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListParseStatic200ResponseInnerStatsInnerMetrics(
            received=payload.get("received")
        )
