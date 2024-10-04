from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.lmc_contactdb.v3.models.search_recipient200_response_recipients_inner_custom_fields_inner_value import (
    SearchRecipient200ResponseRecipientsInnerCustomFieldsInnerValue,
)


class SearchRecipient200ResponseRecipientsInnerCustomFieldsInner:
    def __init__(
        self,
        id: Optional[int] = None,
        name: Optional[str] = None,
        value: Optional[
            SearchRecipient200ResponseRecipientsInnerCustomFieldsInnerValue
        ] = None,
        type: Optional[str] = None,
    ):
        self.id = id
        self.name = name
        self.value = value
        self.type = type

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "name": self.name,
                "value": self.value,
                "type": self.type,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SearchRecipient200ResponseRecipientsInnerCustomFieldsInner(
            id=payload.get("id"),
            name=payload.get("name"),
            value=payload.get("value"),
            type=payload.get("type"),
        )
