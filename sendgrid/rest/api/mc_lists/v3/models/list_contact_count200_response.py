from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListContactCount200Response:
    def __init__(
        self, contact_count: Optional[int] = None, billable_count: Optional[int] = None
    ):
        self.contact_count = contact_count
        self.billable_count = billable_count

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "contact_count": self.contact_count,
                "billable_count": self.billable_count,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListContactCount200Response(
            contact_count=payload.get("contact_count"),
            billable_count=payload.get("billable_count"),
        )
