from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_lists.v3.models.metadata import Metadata



class ListMarketingList200Response:
    def __init__(
            self,
            result: Optional[List[List]]=None,
            metadata: Optional[Metadata]=None
    ):
        self.result=result
        self.metadata=metadata

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "result": self.result,
            "_metadata": self.metadata
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListMarketingList200Response(
            result=payload.get('result'),
            metadata=payload.get('_metadata')
        ) 

