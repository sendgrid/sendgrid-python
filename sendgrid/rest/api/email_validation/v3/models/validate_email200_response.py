from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.email_validation.v3.models.validate_email200_response_result import ValidateEmail200ResponseResult



class ValidateEmail200Response:
    def __init__(
            self,
            result: Optional[ValidateEmail200ResponseResult]=None
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
        return ValidateEmail200Response(
            result=payload.get('result')
        ) 
