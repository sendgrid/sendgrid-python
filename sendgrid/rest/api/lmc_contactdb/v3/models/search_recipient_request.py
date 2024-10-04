from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.lmc_contactdb.v3.models.contactdb_segments_conditions import ContactdbSegmentsConditions



class SearchRecipientRequest:
    def __init__(
            self,
            list_id: Optional[int]=None,
            conditions: Optional[List[ContactdbSegmentsConditions]]=None
    ):
        self.list_id=list_id
        self.conditions=conditions

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "list_id": self.list_id,
            "conditions": self.conditions
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SearchRecipientRequest(
            list_id=payload.get('list_id'),
            conditions=payload.get('conditions')
        ) 

