from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.link_branding.v3.models.default1 import Default1



class UpdateBrandedLinkRequest:
    def __init__(
            self,
            default: Optional[Default1]=None
    ):
        self.default=default

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "default": self.default
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateBrandedLinkRequest(
            default=payload.get('default')
        ) 

