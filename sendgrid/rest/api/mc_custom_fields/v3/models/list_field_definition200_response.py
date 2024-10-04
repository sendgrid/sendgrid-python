from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_custom_fields.v3.models.custom_field_definitions_response import CustomFieldDefinitionsResponse
from sendgrid.rest.api.mc_custom_fields.v3.models.metadata import Metadata
from sendgrid.rest.api.mc_custom_fields.v3.models.reserved_field_definitions_response_inner import ReservedFieldDefinitionsResponseInner



class ListFieldDefinition200Response:
    def __init__(
            self,
            custom_fields: Optional[List[CustomFieldDefinitionsResponse]]=None,
            reserved_fields: Optional[List[ReservedFieldDefinitionsResponseInner]]=None,
            metadata: Optional[Metadata]=None
    ):
        self.custom_fields=custom_fields
        self.reserved_fields=reserved_fields
        self.metadata=metadata

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "custom_fields": self.custom_fields,
            "reserved_fields": self.reserved_fields,
            "_metadata": self.metadata
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListFieldDefinition200Response(
            custom_fields=payload.get('custom_fields'),
            reserved_fields=payload.get('reserved_fields'),
            metadata=payload.get('_metadata')
        ) 

