from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.ip_address_management.v3.models.list_ip_pool200_response_metadata_next_params import ListIpPool200ResponseMetadataNextParams



class ListIpPool200ResponseMetadata:
    def __init__(
            self,
            next_params: Optional[ListIpPool200ResponseMetadataNextParams]=None
    ):
        self.next_params=next_params

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "next_params": self.next_params
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListIpPool200ResponseMetadata(
            next_params=payload.get('next_params')
        ) 

