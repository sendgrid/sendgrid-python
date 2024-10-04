from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SegmentUpdate:
    def __init__(
            self,
            name: Optional[str]=None,
            query_dsl: Optional[str]=None
    ):
        self.name=name
        self.query_dsl=query_dsl

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "name": self.name,
            "query_dsl": self.query_dsl
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SegmentUpdate(
            name=payload.get('name'),
            query_dsl=payload.get('query_dsl')
        ) 

