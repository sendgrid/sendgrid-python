from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.templates.v3.models.generation import Generation



class CreateTemplateRequest:
    def __init__(
            self,
            name: Optional[str]=None,
            generation: Optional[Generation]=None
    ):
        self.name=name
        self.generation=generation

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "name": self.name,
            "generation": self.generation
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CreateTemplateRequest(
            name=payload.get('name'),
            generation=payload.get('generation')
        ) 

