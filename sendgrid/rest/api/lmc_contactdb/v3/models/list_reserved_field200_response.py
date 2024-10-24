from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.lmc_contactdb.v3.models.list_reserved_field200_response_reserved_fields_inner import ListReservedField200ResponseReservedFieldsInner



class ListReservedField200Response:
    def __init__(
            self,
            reserved_fields: Optional[List[ListReservedField200ResponseReservedFieldsInner]]=None
    ):
        self.reserved_fields=reserved_fields

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "reserved_fields": self.reserved_fields
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListReservedField200Response(
            reserved_fields=payload.get('reserved_fields')
        ) 

