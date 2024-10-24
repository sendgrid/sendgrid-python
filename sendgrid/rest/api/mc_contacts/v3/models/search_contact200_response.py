from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_contacts.v3.models.contact_details3 import ContactDetails3
from sendgrid.rest.api.mc_contacts.v3.models.self_metadata import SelfMetadata



class SearchContact200Response:
    def __init__(
            self,
            result: Optional[List[ContactDetails3]]=None,
            metadata: Optional[SelfMetadata]=None,
            contact_count: Optional[float]=None
    ):
        self.result=result
        self.metadata=metadata
        self.contact_count=contact_count

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "result": self.result,
            "_metadata": self.metadata,
            "contact_count": self.contact_count
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SearchContact200Response(
            result=payload.get('result'),
            metadata=payload.get('_metadata'),
            contact_count=payload.get('contact_count')
        ) 

