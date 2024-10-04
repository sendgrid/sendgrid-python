from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_stats.v3.models.link_tracking_metadata import LinkTrackingMetadata
from sendgrid.rest.api.mc_stats.v3.models.singlesends_link_stats_response_results_inner import SinglesendsLinkStatsResponseResultsInner



class SinglesendsLinkStatsResponse:
    def __init__(
            self,
            results: Optional[List[SinglesendsLinkStatsResponseResultsInner]]=None,
            metadata: Optional[LinkTrackingMetadata]=None,
            total_clicks: Optional[int]=None
    ):
        self.results=results
        self.metadata=metadata
        self.total_clicks=total_clicks

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "results": self.results,
            "_metadata": self.metadata,
            "total_clicks": self.total_clicks
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SinglesendsLinkStatsResponse(
            results=payload.get('results'),
            metadata=payload.get('_metadata'),
            total_clicks=payload.get('total_clicks')
        ) 

