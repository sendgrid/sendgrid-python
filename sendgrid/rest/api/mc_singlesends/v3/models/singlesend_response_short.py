from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_singlesends.v3.models.ab_test_summary import AbTestSummary
from sendgrid.rest.api.mc_singlesends.v3.models.status3 import Status3



class SinglesendResponseShort:
    def __init__(
            self,
            id: Optional[str]=None,
            name: Optional[str]=None,
            abtest: Optional[AbTestSummary]=None,
            status: Optional[Status3]=None,
            categories: Optional[List[str]]=None,
            send_at: Optional[datetime]=None,
            is_abtest: Optional[bool]=None,
            updated_at: Optional[datetime]=None,
            created_at: Optional[datetime]=None
    ):
        self.id=id
        self.name=name
        self.abtest=abtest
        self.status=status
        self.categories=categories
        self.send_at=send_at
        self.is_abtest=is_abtest
        self.updated_at=updated_at
        self.created_at=created_at

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "name": self.name,
            "abtest": self.abtest,
            "status": self.status,
            "categories": self.categories,
            "send_at": self.send_at,
            "is_abtest": self.is_abtest,
            "updated_at": self.updated_at,
            "created_at": self.created_at
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SinglesendResponseShort(
            id=payload.get('id'),
            name=payload.get('name'),
            abtest=payload.get('abtest'),
            status=payload.get('status'),
            categories=payload.get('categories'),
            send_at=payload.get('send_at'),
            is_abtest=payload.get('is_abtest'),
            updated_at=payload.get('updated_at'),
            created_at=payload.get('created_at')
        ) 

