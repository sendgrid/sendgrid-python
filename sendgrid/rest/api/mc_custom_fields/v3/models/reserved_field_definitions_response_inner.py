from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_custom_fields.v3.models.field_type1 import FieldType1



class ReservedFieldDefinitionsResponseInner:
    def __init__(
            self,
            name: Optional[str]=None,
            field_type: Optional[FieldType1]=None,
            read_only: Optional[bool]=None
    ):
        self.name=name
        self.field_type=field_type
        self.read_only=read_only

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "name": self.name,
            "field_type": self.field_type,
            "read_only": self.read_only
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ReservedFieldDefinitionsResponseInner(
            name=payload.get('name'),
            field_type=payload.get('field_type'),
            read_only=payload.get('read_only')
        ) 

