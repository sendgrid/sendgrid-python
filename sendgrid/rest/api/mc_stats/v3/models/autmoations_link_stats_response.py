from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_stats.v3.models.autmoations_link_stats_response_results_inner import (
    AutmoationsLinkStatsResponseResultsInner,
)
from sendgrid.rest.api.mc_stats.v3.models.link_tracking_metadata import (
    LinkTrackingMetadata,
)


class AutmoationsLinkStatsResponse:
    def __init__(
        self,
        results: Optional[List[AutmoationsLinkStatsResponseResultsInner]] = None,
        total_clicks: Optional[int] = None,
        metadata: Optional[LinkTrackingMetadata] = None,
    ):
        self.results = results
        self.total_clicks = total_clicks
        self.metadata = metadata

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "results": self.results,
                "total_clicks": self.total_clicks,
                "_metadata": self.metadata,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AutmoationsLinkStatsResponse(
            results=payload.get("results"),
            total_clicks=payload.get("total_clicks"),
            metadata=payload.get("_metadata"),
        )
