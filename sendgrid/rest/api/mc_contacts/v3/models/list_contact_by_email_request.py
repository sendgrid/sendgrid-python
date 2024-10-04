from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListContactByEmailRequest:
    def __init__(
        self,
        emails: Optional[List[str]] = None,
        phone_number_id: Optional[str] = None,
        external_id: Optional[str] = None,
        anonymous_id: Optional[str] = None,
    ):
        self.emails = emails
        self.phone_number_id = phone_number_id
        self.external_id = external_id
        self.anonymous_id = anonymous_id

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "emails": self.emails,
                "phone_number_id": self.phone_number_id,
                "external_id": self.external_id,
                "anonymous_id": self.anonymous_id,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListContactByEmailRequest(
            emails=payload.get("emails"),
            phone_number_id=payload.get("phone_number_id"),
            external_id=payload.get("external_id"),
            anonymous_id=payload.get("anonymous_id"),
        )
