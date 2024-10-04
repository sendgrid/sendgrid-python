from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_stats.v3.models.ab_phase import AbPhase
from sendgrid.rest.api.mc_stats.v3.models.metrics import Metrics


class SinglesendsResponseResultsInner:
    def __init__(
        self,
        id: Optional[str] = None,
        ab_variation: Optional[str] = None,
        ab_phase: Optional[AbPhase] = None,
        aggregation: Optional[str] = None,
        stats: Optional[Metrics] = None,
    ):
        self.id = id
        self.ab_variation = ab_variation
        self.ab_phase = ab_phase
        self.aggregation = aggregation
        self.stats = stats

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "ab_variation": self.ab_variation,
                "ab_phase": self.ab_phase,
                "aggregation": self.aggregation,
                "stats": self.stats,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SinglesendsResponseResultsInner(
            id=payload.get("id"),
            ab_variation=payload.get("ab_variation"),
            ab_phase=payload.get("ab_phase"),
            aggregation=payload.get("aggregation"),
            stats=payload.get("stats"),
        )
