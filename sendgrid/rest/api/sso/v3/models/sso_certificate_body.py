from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SsoCertificateBody:
    def __init__(
            self,
            public_certificate: Optional[str]=None,
            id: Optional[float]=None,
            not_before: Optional[float]=None,
            not_after: Optional[float]=None,
            intergration_id: Optional[str]=None
    ):
        self.public_certificate=public_certificate
        self.id=id
        self.not_before=not_before
        self.not_after=not_after
        self.intergration_id=intergration_id

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "public_certificate": self.public_certificate,
            "id": self.id,
            "not_before": self.not_before,
            "not_after": self.not_after,
            "intergration_id": self.intergration_id
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SsoCertificateBody(
            public_certificate=payload.get('public_certificate'),
            id=payload.get('id'),
            not_before=payload.get('not_before'),
            not_after=payload.get('not_after'),
            intergration_id=payload.get('intergration_id')
        ) 

