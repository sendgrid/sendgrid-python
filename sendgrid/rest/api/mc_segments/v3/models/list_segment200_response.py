from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_segments.v3.models.segment_summary import SegmentSummary



class ListSegment200Response:
    def __init__(
            self,
            results: Optional[List[SegmentSummary]]=None
    ):
        self.results=results

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "results": self.results
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListSegment200Response(
            results=payload.get('results')
        ) 

