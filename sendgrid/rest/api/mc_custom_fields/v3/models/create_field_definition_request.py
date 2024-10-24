from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_custom_fields.v3.models.field_type import FieldType



class CreateFieldDefinitionRequest:
    def __init__(
            self,
            name: Optional[str]=None,
            field_type: Optional[FieldType]=None
    ):
        self.name=name
        self.field_type=field_type

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "name": self.name,
            "field_type": self.field_type
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CreateFieldDefinitionRequest(
            name=payload.get('name'),
            field_type=payload.get('field_type')
        ) 

