from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.subusers.v3.models.subuser_stats_stats_inner_metrics import (
    SubuserStatsStatsInnerMetrics,
)


class SubuserStatsStatsInner:
    def __init__(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        metrics: Optional[SubuserStatsStatsInnerMetrics] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.metrics = metrics
        self.name = name
        self.type = type

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "metrics": self.metrics,
                "name": self.name,
                "type": self.type,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SubuserStatsStatsInner(
            first_name=payload.get("first_name"),
            last_name=payload.get("last_name"),
            metrics=payload.get("metrics"),
            name=payload.get("name"),
            type=payload.get("type"),
        )
