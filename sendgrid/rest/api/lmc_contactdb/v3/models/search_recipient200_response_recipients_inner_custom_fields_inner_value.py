from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SearchRecipient200ResponseRecipientsInnerCustomFieldsInnerValue:
    def __init__(
            self,
    ):

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SearchRecipient200ResponseRecipientsInnerCustomFieldsInnerValue(
        ) 

