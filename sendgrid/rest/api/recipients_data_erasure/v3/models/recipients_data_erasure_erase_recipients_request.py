from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class RecipientsDataErasureEraseRecipientsRequest:
    def __init__(
            self,
            email_addresses: Optional[List[str]]=None
    ):
        self.email_addresses=email_addresses

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "email_addresses": self.email_addresses
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return RecipientsDataErasureEraseRecipientsRequest(
            email_addresses=payload.get('email_addresses')
        ) 

