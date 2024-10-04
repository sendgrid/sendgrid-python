from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_stats.v3.models.automations_response_results_inner import (
    AutomationsResponseResultsInner,
)
from sendgrid.rest.api.mc_stats.v3.models.metadata import Metadata


class AutomationsResponse:
    def __init__(
        self,
        results: Optional[List[AutomationsResponseResultsInner]] = None,
        metadata: Optional[Metadata] = None,
    ):
        self.results = results
        self.metadata = metadata

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "results": self.results,
                "_metadata": self.metadata,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AutomationsResponse(
            results=payload.get("results"), metadata=payload.get("_metadata")
        )
