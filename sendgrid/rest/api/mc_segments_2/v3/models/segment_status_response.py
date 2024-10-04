from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class SegmentStatusResponse:
    def __init__(
        self,
        query_validation: Optional[str] = None,
        error_message: Optional[str] = None,
    ):
        self.query_validation = query_validation
        self.error_message = error_message

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "query_validation": self.query_validation,
                "error_message": self.error_message,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SegmentStatusResponse(
            query_validation=payload.get("query_validation"),
            error_message=payload.get("error_message"),
        )
