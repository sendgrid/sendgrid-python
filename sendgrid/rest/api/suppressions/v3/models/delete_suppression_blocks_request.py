from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class DeleteSuppressionBlocksRequest:
    def __init__(
        self, delete_all: Optional[bool] = None, emails: Optional[List[str]] = None
    ):
        self.delete_all = delete_all
        self.emails = emails

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "delete_all": self.delete_all,
                "emails": self.emails,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return DeleteSuppressionBlocksRequest(
            delete_all=payload.get("delete_all"), emails=payload.get("emails")
        )
