from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.ip_address_management.v3.models.list_ip_assigned_to_ip_pool200_response_metadata import ListIpAssignedToIpPool200ResponseMetadata
from sendgrid.rest.api.ip_address_management.v3.models.list_ip_assigned_to_ip_pool200_response_result_inner import ListIpAssignedToIpPool200ResponseResultInner



class ListIpAssignedToIpPool200Response:
    def __init__(
            self,
            result: Optional[List[ListIpAssignedToIpPool200ResponseResultInner]]=None,
            metadata: Optional[ListIpAssignedToIpPool200ResponseMetadata]=None
    ):
        self.result=result
        self.metadata=metadata

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "result": self.result,
            "_metadata": self.metadata
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListIpAssignedToIpPool200Response(
            result=payload.get('result'),
            metadata=payload.get('_metadata')
        ) 

