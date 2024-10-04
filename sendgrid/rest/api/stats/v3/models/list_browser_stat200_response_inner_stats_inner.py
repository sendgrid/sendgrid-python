from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.stats.v3.models.advanced_stats_clicks import AdvancedStatsClicks


class ListBrowserStat200ResponseInnerStatsInner:
    def __init__(
        self,
        type: Optional[str] = None,
        name: Optional[str] = None,
        metrics: Optional[AdvancedStatsClicks] = None,
    ):
        self.type = type
        self.name = name
        self.metrics = metrics

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "type": self.type,
                "name": self.name,
                "metrics": self.metrics,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListBrowserStat200ResponseInnerStatsInner(
            type=payload.get("type"),
            name=payload.get("name"),
            metrics=payload.get("metrics"),
        )
