from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.stats.v3.models.stats_advanced_global_stats import (
    StatsAdvancedGlobalStats,
)


class ListStat200ResponseInnerStatsInner:
    def __init__(self, metrics: Optional[StatsAdvancedGlobalStats] = None):
        self.metrics = metrics

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"metrics": self.metrics}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListStat200ResponseInnerStatsInner(metrics=payload.get("metrics"))
