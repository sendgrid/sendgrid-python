from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ListSubUserAssignedToIp200ResponseMetadataNextParams:
    def __init__(
            self,
            after_key: Optional[str]=None,
            limit: Optional[str]=None
    ):
        self.after_key=after_key
        self.limit=limit

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "after_key": self.after_key,
            "limit": self.limit
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListSubUserAssignedToIp200ResponseMetadataNextParams(
            after_key=payload.get('after_key'),
            limit=payload.get('limit')
        ) 

