from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.ip_address_management.v3.models.list_sub_user_assigned_to_ip200_response_metadata import ListSubUserAssignedToIp200ResponseMetadata



class ListSubUserAssignedToIp200Response:
    def __init__(
            self,
            result: Optional[List[str]]=None,
            metadata: Optional[ListSubUserAssignedToIp200ResponseMetadata]=None
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
        return ListSubUserAssignedToIp200Response(
            result=payload.get('result'),
            metadata=payload.get('_metadata')
        ) 

