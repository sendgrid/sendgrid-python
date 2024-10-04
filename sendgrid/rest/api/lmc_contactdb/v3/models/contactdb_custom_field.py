from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.lmc_contactdb.v3.models.type import Type



class ContactdbCustomField:
    def __init__(
            self,
            name: Optional[str]=None,
            type: Optional[Type]=None
    ):
        self.name=name
        self.type=type

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "name": self.name,
            "type": self.type
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactdbCustomField(
            name=payload.get('name'),
            type=payload.get('type')
        ) 

