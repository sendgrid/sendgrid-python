from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.suppressions.v3.models.get_suppression_bounces_classifications200_response_result_inner import GetSuppressionBouncesClassifications200ResponseResultInner



class GetSuppressionBouncesClassifications200Response:
    def __init__(
            self,
            result: Optional[List[GetSuppressionBouncesClassifications200ResponseResultInner]]=None
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
        return GetSuppressionBouncesClassifications200Response(
            result=payload.get('result')
        ) 

