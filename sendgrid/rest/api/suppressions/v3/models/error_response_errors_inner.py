from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ErrorResponseErrorsInner:
    def __init__(
        self,
        message: Optional[str] = None,
        field: Optional[str] = None,
        help: Optional[object] = None,
    ):
        self.message = message
        self.field = field
        self.help = help

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "message": self.message,
                "field": self.field,
                "help": self.help,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ErrorResponseErrorsInner(
            message=payload.get("message"),
            field=payload.get("field"),
            help=payload.get("help"),
        )
