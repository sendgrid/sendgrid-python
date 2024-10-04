from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ValidateEmail200ResponseResultChecksAdditional:
    def __init__(
            self,
            has_known_bounces: Optional[bool]=None,
            has_suspected_bounces: Optional[bool]=None
    ):
        self.has_known_bounces=has_known_bounces
        self.has_suspected_bounces=has_suspected_bounces

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "has_known_bounces": self.has_known_bounces,
            "has_suspected_bounces": self.has_suspected_bounces
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ValidateEmail200ResponseResultChecksAdditional(
            has_known_bounces=payload.get('has_known_bounces'),
            has_suspected_bounces=payload.get('has_suspected_bounces')
        ) 

