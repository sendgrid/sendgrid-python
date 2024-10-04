from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class PostPatchIntegrationRequest:
    def __init__(
            self,
            name: Optional[str]=None,
            enabled: Optional[bool]=None,
            signin_url: Optional[str]=None,
            signout_url: Optional[str]=None,
            entity_id: Optional[str]=None,
            completed_integration: Optional[bool]=None
    ):
        self.name=name
        self.enabled=enabled
        self.signin_url=signin_url
        self.signout_url=signout_url
        self.entity_id=entity_id
        self.completed_integration=completed_integration

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "name": self.name,
            "enabled": self.enabled,
            "signin_url": self.signin_url,
            "signout_url": self.signout_url,
            "entity_id": self.entity_id,
            "completed_integration": self.completed_integration
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return PostPatchIntegrationRequest(
            name=payload.get('name'),
            enabled=payload.get('enabled'),
            signin_url=payload.get('signin_url'),
            signout_url=payload.get('signout_url'),
            entity_id=payload.get('entity_id'),
            completed_integration=payload.get('completed_integration')
        ) 

