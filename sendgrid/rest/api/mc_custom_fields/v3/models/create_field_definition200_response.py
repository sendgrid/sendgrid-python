from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_custom_fields.v3.models.field_type2 import FieldType2
from sendgrid.rest.api.mc_custom_fields.v3.models.metadata import Metadata


class CreateFieldDefinition200Response:
    def __init__(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        field_type: Optional[FieldType2] = None,
        metadata: Optional[Metadata] = None,
    ):
        self.id = id
        self.name = name
        self.field_type = field_type
        self.metadata = metadata

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "name": self.name,
                "field_type": self.field_type,
                "_metadata": self.metadata,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CreateFieldDefinition200Response(
            id=payload.get("id"),
            name=payload.get("name"),
            field_type=payload.get("field_type"),
            metadata=payload.get("_metadata"),
        )
