from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.ip_warmup.v3.models.stop_ip_warm_up404_response_errors_inner import StopIpWarmUp404ResponseErrorsInner



class StopIpWarmUp404Response:
    def __init__(
            self,
            errors: Optional[List[StopIpWarmUp404ResponseErrorsInner]]=None
    ):
        self.errors=errors

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "errors": self.errors
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return StopIpWarmUp404Response(
            errors=payload.get('errors')
        ) 

