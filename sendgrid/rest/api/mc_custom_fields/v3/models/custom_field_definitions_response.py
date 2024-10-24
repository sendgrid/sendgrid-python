from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_custom_fields.v3.models.field_type2 import FieldType2



class CustomFieldDefinitionsResponse:
    def __init__(
            self,
            id: Optional[str]=None,
            name: Optional[str]=None,
            field_type: Optional[FieldType2]=None
    ):
        self.id=id
        self.name=name
        self.field_type=field_type

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "name": self.name,
            "field_type": self.field_type
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CustomFieldDefinitionsResponse(
            id=payload.get('id'),
            name=payload.get('name'),
            field_type=payload.get('field_type')
        ) 
