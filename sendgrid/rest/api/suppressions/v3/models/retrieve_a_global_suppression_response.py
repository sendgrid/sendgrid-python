from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class RetrieveAGlobalSuppressionResponse:
    def __init__(
            self,
            recipient_email: Optional[str]=None
    ):
        self.recipient_email=recipient_email

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "recipient_email": self.recipient_email
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return RetrieveAGlobalSuppressionResponse(
            recipient_email=payload.get('recipient_email')
        ) 

