from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_contacts.v3.models.file_type1 import FileType1


class ImportContactRequest:
    def __init__(
        self,
        list_ids: Optional[List[str]] = None,
        file_type: Optional[FileType1] = None,
        field_mappings: Optional[List[str]] = None,
    ):
        self.list_ids = list_ids
        self.file_type = file_type
        self.field_mappings = field_mappings

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "list_ids": self.list_ids,
                "file_type": self.file_type,
                "field_mappings": self.field_mappings,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ImportContactRequest(
            list_ids=payload.get("list_ids"),
            file_type=payload.get("file_type"),
            field_mappings=payload.get("field_mappings"),
        )
