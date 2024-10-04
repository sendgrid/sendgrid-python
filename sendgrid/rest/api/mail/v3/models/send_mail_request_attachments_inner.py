from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mail.v3.models.disposition import Disposition


class SendMailRequestAttachmentsInner:
    def __init__(
        self,
        content: Optional[str] = None,
        type: Optional[str] = None,
        filename: Optional[str] = None,
        disposition: Optional[Disposition] = None,
        content_id: Optional[str] = None,
    ):
        self.content = content
        self.type = type
        self.filename = filename
        self.disposition = disposition
        self.content_id = content_id

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "content": self.content,
                "type": self.type,
                "filename": self.filename,
                "disposition": self.disposition,
                "content_id": self.content_id,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendMailRequestAttachmentsInner(
            content=payload.get("content"),
            type=payload.get("type"),
            filename=payload.get("filename"),
            disposition=payload.get("disposition"),
            content_id=payload.get("content_id"),
        )
