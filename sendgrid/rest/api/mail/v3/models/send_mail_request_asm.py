from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SendMailRequestAsm:
    def __init__(
            self,
            group_id: Optional[int]=None,
            groups_to_display: Optional[List[int]]=None
    ):
        self.group_id=group_id
        self.groups_to_display=groups_to_display

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "group_id": self.group_id,
            "groups_to_display": self.groups_to_display
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendMailRequestAsm(
            group_id=payload.get('group_id'),
            groups_to_display=payload.get('groups_to_display')
        ) 

