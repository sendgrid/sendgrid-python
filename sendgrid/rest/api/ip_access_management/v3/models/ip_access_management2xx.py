from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.ip_access_management.v3.models.ip_access_management2xx_result_inner import IpAccessManagement2xxResultInner



class IpAccessManagement2xx:
    def __init__(
            self,
            result: Optional[List[IpAccessManagement2xxResultInner]]=None
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
        return IpAccessManagement2xx(
            result=payload.get('result')
        ) 

