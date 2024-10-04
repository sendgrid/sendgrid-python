from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_stats.v3.models.metadata import Metadata
from sendgrid.rest.api.mc_stats.v3.models.singlesends_response_results_inner import SinglesendsResponseResultsInner



class SinglesendsResponse:
    def __init__(
            self,
            results: Optional[List[SinglesendsResponseResultsInner]]=None,
            metadata: Optional[Metadata]=None
    ):
        self.results=results
        self.metadata=metadata

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "results": self.results,
            "_metadata": self.metadata
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SinglesendsResponse(
            results=payload.get('results'),
            metadata=payload.get('_metadata')
        ) 

