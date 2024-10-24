from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_designs.v3.models.editor import Editor



class DesignOutputSummary:
    def __init__(
            self,
            id: Optional[str]=None,
            updated_at: Optional[str]=None,
            created_at: Optional[str]=None,
            thumbnail_url: Optional[str]=None,
            name: Optional[str]=None,
            editor: Optional[Editor]=None
    ):
        self.id=id
        self.updated_at=updated_at
        self.created_at=created_at
        self.thumbnail_url=thumbnail_url
        self.name=name
        self.editor=editor

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "updated_at": self.updated_at,
            "created_at": self.created_at,
            "thumbnail_url": self.thumbnail_url,
            "name": self.name,
            "editor": self.editor
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return DesignOutputSummary(
            id=payload.get('id'),
            updated_at=payload.get('updated_at'),
            created_at=payload.get('created_at'),
            thumbnail_url=payload.get('thumbnail_url'),
            name=payload.get('name'),
            editor=payload.get('editor')
        ) 

