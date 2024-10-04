from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_senders.v3.models.sender import Sender



class ListSender200Response:
    def __init__(
            self,
            results: Optional[List[Sender]]=None
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
        return ListSender200Response(
            results=payload.get('results')
        ) 

