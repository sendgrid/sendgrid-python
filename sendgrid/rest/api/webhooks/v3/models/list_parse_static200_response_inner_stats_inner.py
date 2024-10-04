from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.webhooks.v3.models.list_parse_static200_response_inner_stats_inner_metrics import (
    ListParseStatic200ResponseInnerStatsInnerMetrics,
)


class ListParseStatic200ResponseInnerStatsInner:
    def __init__(
        self, metrics: Optional[ListParseStatic200ResponseInnerStatsInnerMetrics] = None
    ):
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
        return ListParseStatic200ResponseInnerStatsInner(metrics=payload.get("metrics"))
