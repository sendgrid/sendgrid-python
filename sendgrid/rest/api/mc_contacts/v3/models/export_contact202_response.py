from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_contacts.v3.models.metadata import Metadata


class ExportContact202Response:
    def __init__(self, metadata: Optional[Metadata] = None, id: Optional[str] = None):
        self.metadata = metadata
        self.id = id

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"_metadata": self.metadata, "id": self.id}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ExportContact202Response(
            metadata=payload.get("_metadata"), id=payload.get("id")
        )
