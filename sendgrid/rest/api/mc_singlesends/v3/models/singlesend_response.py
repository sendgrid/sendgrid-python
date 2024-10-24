from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_singlesends.v3.models.singlesend_response_email_config import SinglesendResponseEmailConfig
from sendgrid.rest.api.mc_singlesends.v3.models.singlesend_response_send_to import SinglesendResponseSendTo
from sendgrid.rest.api.mc_singlesends.v3.models.singlesend_response_warnings_inner import SinglesendResponseWarningsInner
from sendgrid.rest.api.mc_singlesends.v3.models.status2 import Status2



class SinglesendResponse:
    def __init__(
            self,
            id: Optional[str]=None,
            name: Optional[str]=None,
            status: Optional[Status2]=None,
            categories: Optional[List[str]]=None,
            send_at: Optional[datetime]=None,
            send_to: Optional[SinglesendResponseSendTo]=None,
            updated_at: Optional[datetime]=None,
            created_at: Optional[datetime]=None,
            email_config: Optional[SinglesendResponseEmailConfig]=None,
            warnings: Optional[List[SinglesendResponseWarningsInner]]=None
    ):
        self.id=id
        self.name=name
        self.status=status
        self.categories=categories
        self.send_at=send_at
        self.send_to=send_to
        self.updated_at=updated_at
        self.created_at=created_at
        self.email_config=email_config
        self.warnings=warnings

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "categories": self.categories,
            "send_at": self.send_at,
            "send_to": self.send_to,
            "updated_at": self.updated_at,
            "created_at": self.created_at,
            "email_config": self.email_config,
            "warnings": self.warnings
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SinglesendResponse(
            id=payload.get('id'),
            name=payload.get('name'),
            status=payload.get('status'),
            categories=payload.get('categories'),
            send_at=payload.get('send_at'),
            send_to=payload.get('send_to'),
            updated_at=payload.get('updated_at'),
            created_at=payload.get('created_at'),
            email_config=payload.get('email_config'),
            warnings=payload.get('warnings')
        ) 

