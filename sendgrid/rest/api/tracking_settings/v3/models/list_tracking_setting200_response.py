from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.tracking_settings.v3.models.list_tracking_setting200_response_result_inner import ListTrackingSetting200ResponseResultInner



class ListTrackingSetting200Response:
    def __init__(
            self,
            result: Optional[List[ListTrackingSetting200ResponseResultInner]]=None
    ):
        self.result=result

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "result": self.result
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListTrackingSetting200Response(
            result=payload.get('result')
        ) 

