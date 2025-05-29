from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.templates.v3.models.generation1 import Generation1
from sendgrid.rest.api.templates.v3.models.transactional_template_warning import TransactionalTemplateWarning
from sendgrid.rest.api.templates.v3.models.transactional_templates_version_output_lean import TransactionalTemplatesVersionOutputLean



class TransactionalTemplate:
    def __init__(
            self,
            id: Optional[str]=None,
            name: Optional[str]=None,
            generation: Optional[Generation1]=None,
            updated_at: Optional[str]=None,
            versions: Optional[List[TransactionalTemplatesVersionOutputLean]]=None,
            warning: Optional[TransactionalTemplateWarning]=None
    ):
        self.id=id
        self.name=name
        self.generation=generation
        self.updated_at=updated_at
        self.versions=versions
        self.warning=warning

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "name": self.name,
            "generation": self.generation,
            "updated_at": self.updated_at,
            "versions": self.versions,
            "warning": self.warning
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return TransactionalTemplate(
            id=payload.get('id'),
            name=payload.get('name'),
            generation=payload.get('generation'),
            updated_at=payload.get('updated_at'),
            versions=payload.get('versions'),
            warning=payload.get('warning')
        ) 

