from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.domain_authentication.v3.models.email_dns_record400_response_errors import EmailDnsRecord400ResponseErrors



class EmailDnsRecord400Response:
    def __init__(
            self,
            errors: Optional[EmailDnsRecord400ResponseErrors]=None
    ):
        self.errors=errors

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "errors": self.errors
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return EmailDnsRecord400Response(
            errors=payload.get('errors')
        ) 

