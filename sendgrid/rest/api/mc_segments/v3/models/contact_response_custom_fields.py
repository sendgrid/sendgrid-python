from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ContactResponseCustomFields:
    def __init__(
        self,
        custom_field_name1: Optional[str] = None,
        custom_field_name2: Optional[str] = None,
    ):
        self.custom_field_name1 = custom_field_name1
        self.custom_field_name2 = custom_field_name2

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "custom_field_name1": self.custom_field_name1,
                "custom_field_name2": self.custom_field_name2,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactResponseCustomFields(
            custom_field_name1=payload.get("custom_field_name1"),
            custom_field_name2=payload.get("custom_field_name2"),
        )
