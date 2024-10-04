from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ValidateEmail200ResponseResultChecksDomain:
    def __init__(
            self,
            has_valid_address_syntax: Optional[bool]=None,
            has_mx_or_a_record: Optional[bool]=None,
            is_suspected_disposable_address: Optional[bool]=None
    ):
        self.has_valid_address_syntax=has_valid_address_syntax
        self.has_mx_or_a_record=has_mx_or_a_record
        self.is_suspected_disposable_address=is_suspected_disposable_address

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "has_valid_address_syntax": self.has_valid_address_syntax,
            "has_mx_or_a_record": self.has_mx_or_a_record,
            "is_suspected_disposable_address": self.is_suspected_disposable_address
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ValidateEmail200ResponseResultChecksDomain(
            has_valid_address_syntax=payload.get('has_valid_address_syntax'),
            has_mx_or_a_record=payload.get('has_mx_or_a_record'),
            is_suspected_disposable_address=payload.get('is_suspected_disposable_address')
        ) 

