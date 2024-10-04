from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.email_validation.v3.models.file_type import FileType


class ListEmailJobForVerificationRequest:
    def __init__(self, file_type: Optional[FileType] = None):
        self.file_type = file_type

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"file_type": self.file_type}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListEmailJobForVerificationRequest(file_type=payload.get("file_type"))
