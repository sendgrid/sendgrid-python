from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class DeleteSubUsersFromIpRequest:
    def __init__(
            self,
            subusers: Optional[List[str]]=None
    ):
        self.subusers=subusers

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "subusers": self.subusers
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return DeleteSubUsersFromIpRequest(
            subusers=payload.get('subusers')
        ) 

