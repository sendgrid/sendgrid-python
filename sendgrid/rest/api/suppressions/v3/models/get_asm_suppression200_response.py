from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.suppressions.v3.models.get_asm_suppression200_response_suppressions_inner import (
    GetAsmSuppression200ResponseSuppressionsInner,
)


class GetAsmSuppression200Response:
    def __init__(
        self,
        suppressions: Optional[
            List[GetAsmSuppression200ResponseSuppressionsInner]
        ] = None,
    ):
        self.suppressions = suppressions

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"suppressions": self.suppressions}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetAsmSuppression200Response(suppressions=payload.get("suppressions"))
