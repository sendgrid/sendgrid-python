from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.ips.v3.models.list_remaining_ip_count200_response_results_inner import ListRemainingIpCount200ResponseResultsInner



class ListRemainingIpCount200Response:
    def __init__(
            self,
            results: Optional[List[ListRemainingIpCount200ResponseResultsInner]]=None
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
        return ListRemainingIpCount200Response(
            results=payload.get('results')
        ) 

