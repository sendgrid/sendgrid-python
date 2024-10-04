from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_contacts.v3.models.contact_request import ContactRequest


class UpdateContactRequest:
    def __init__(
        self,
        list_ids: Optional[List[str]] = None,
        contacts: Optional[List[ContactRequest]] = None,
    ):
        self.list_ids = list_ids
        self.contacts = contacts

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "list_ids": self.list_ids,
                "contacts": self.contacts,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateContactRequest(
            list_ids=payload.get("list_ids"), contacts=payload.get("contacts")
        )
