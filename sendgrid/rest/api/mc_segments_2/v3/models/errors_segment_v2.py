from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_segments_2.v3.models.errors_segment_v2_errors_inner import (
    ErrorsSegmentV2ErrorsInner,
)


class ErrorsSegmentV2:
    def __init__(self, errors: Optional[List[ErrorsSegmentV2ErrorsInner]] = None):
        self.errors = errors

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"errors": self.errors}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ErrorsSegmentV2(errors=payload.get("errors"))
