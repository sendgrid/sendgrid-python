from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SinglesendResponseSendTo:
    def __init__(
            self,
            list_ids: Optional[List[str]]=None,
            segment_ids: Optional[List[str]]=None,
            all: Optional[bool]=None
    ):
        self.list_ids=list_ids
        self.segment_ids=segment_ids
        self.all=all

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "list_ids": self.list_ids,
            "segment_ids": self.segment_ids,
            "all": self.all
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SinglesendResponseSendTo(
            list_ids=payload.get('list_ids'),
            segment_ids=payload.get('segment_ids'),
            all=payload.get('all')
        ) 

