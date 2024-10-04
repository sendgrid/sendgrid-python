from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.stats.v3.models.category_stats_stats_inner_metrics import (
    CategoryStatsStatsInnerMetrics,
)


class CategoryStatsStatsInner:
    def __init__(
        self,
        metrics: Optional[CategoryStatsStatsInnerMetrics] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
    ):
        self.metrics = metrics
        self.name = name
        self.type = type

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
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
        return CategoryStatsStatsInner(
            metrics=payload.get("metrics"),
            name=payload.get("name"),
            type=payload.get("type"),
        )
