from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_custom_fields.v3.models.custom_fields_error import (
    CustomFieldsError,
)


class CreateFieldDefinition400Response:
    def __init__(self, errors: Optional[List[CustomFieldsError]] = None):
        self.errors = errors

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"errors": self.errors}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CreateFieldDefinition400Response(errors=payload.get("errors"))
