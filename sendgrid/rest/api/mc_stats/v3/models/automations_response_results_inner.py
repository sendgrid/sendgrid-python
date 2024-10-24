from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_stats.v3.models.metrics import Metrics



class AutomationsResponseResultsInner:
    def __init__(
            self,
            id: Optional[str]=None,
            aggregation: Optional[str]=None,
            step_id: Optional[str]=None,
            stats: Optional[Metrics]=None
    ):
        self.id=id
        self.aggregation=aggregation
        self.step_id=step_id
        self.stats=stats

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "aggregation": self.aggregation,
            "step_id": self.step_id,
            "stats": self.stats
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AutomationsResponseResultsInner(
            id=payload.get('id'),
            aggregation=payload.get('aggregation'),
            step_id=payload.get('step_id'),
            stats=payload.get('stats')
        ) 

