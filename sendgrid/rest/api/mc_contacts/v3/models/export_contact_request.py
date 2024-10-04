from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_contacts.v3.models.export_contact_request_notifications import (
    ExportContactRequestNotifications,
)
from sendgrid.rest.api.mc_contacts.v3.models.file_type import FileType


class ExportContactRequest:
    def __init__(
        self,
        list_ids: Optional[List[str]] = None,
        segment_ids: Optional[List[str]] = None,
        notifications: Optional[ExportContactRequestNotifications] = None,
        file_type: Optional[FileType] = None,
        max_file_size: Optional[int] = None,
    ):
        self.list_ids = list_ids
        self.segment_ids = segment_ids
        self.notifications = notifications
        self.file_type = file_type
        self.max_file_size = max_file_size

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "list_ids": self.list_ids,
                "segment_ids": self.segment_ids,
                "notifications": self.notifications,
                "file_type": self.file_type,
                "max_file_size": self.max_file_size,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ExportContactRequest(
            list_ids=payload.get("list_ids"),
            segment_ids=payload.get("segment_ids"),
            notifications=payload.get("notifications"),
            file_type=payload.get("file_type"),
            max_file_size=payload.get("max_file_size"),
        )
