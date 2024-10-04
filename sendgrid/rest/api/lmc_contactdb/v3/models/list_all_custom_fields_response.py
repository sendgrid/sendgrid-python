from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.lmc_contactdb.v3.models.contactdb_custom_field_id2xx import ContactdbCustomFieldId2xx



class ListAllCustomFieldsResponse:
    def __init__(
            self,
            custom_fields: Optional[List[ContactdbCustomFieldId2xx]]=None
    ):
        self.custom_fields=custom_fields

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "custom_fields": self.custom_fields
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListAllCustomFieldsResponse(
            custom_fields=payload.get('custom_fields')
        ) 

