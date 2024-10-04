from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListExportContact200ResponseMetadata:
    def __init__(
        self,
        prev: Optional[str] = None,
        var_self: Optional[str] = None,
        next: Optional[str] = None,
    ):
        self.prev = prev
        self.var_self = var_self
        self.next = next

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "prev": self.prev,
                "self": self.var_self,
                "next": self.next,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListExportContact200ResponseMetadata(
            prev=payload.get("prev"),
            var_self=payload.get("self"),
            next=payload.get("next"),
        )
