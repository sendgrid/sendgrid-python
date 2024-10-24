from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_lists.v3.models.self_metadata import SelfMetadata



class List:
    def __init__(
            self,
            id: Optional[str]=None,
            name: Optional[str]=None,
            contact_count: Optional[int]=None,
            metadata: Optional[SelfMetadata]=None
    ):
        self.id=id
        self.name=name
        self.contact_count=contact_count
        self.metadata=metadata

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "name": self.name,
            "contact_count": self.contact_count,
            "_metadata": self.metadata
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return List(
            id=payload.get('id'),
            name=payload.get('name'),
            contact_count=payload.get('contact_count'),
            metadata=payload.get('_metadata')
        ) 

