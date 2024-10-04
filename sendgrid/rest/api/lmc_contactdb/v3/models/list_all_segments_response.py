from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.lmc_contactdb.v3.models.contactdb_segments import (
    ContactdbSegments,
)


class ListAllSegmentsResponse:
    def __init__(self, segments: Optional[List[ContactdbSegments]] = None):
        self.segments = segments

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"segments": self.segments}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListAllSegmentsResponse(segments=payload.get("segments"))
