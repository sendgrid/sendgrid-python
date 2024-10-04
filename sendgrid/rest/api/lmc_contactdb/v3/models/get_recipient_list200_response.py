from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.lmc_contactdb.v3.models.contactdb_list2xx import ContactdbList2xx



class GetRecipientList200Response:
    def __init__(
            self,
            lists: Optional[List[ContactdbList2xx]]=None
    ):
        self.lists=lists

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "lists": self.lists
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetRecipientList200Response(
            lists=payload.get('lists')
        ) 

