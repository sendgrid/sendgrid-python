from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class EmailDnsRecordRequest:
    def __init__(
        self,
        link_id: Optional[int] = None,
        domain_id: Optional[int] = None,
        email: Optional[str] = None,
        message: Optional[str] = None,
    ):
        self.link_id = link_id
        self.domain_id = domain_id
        self.email = email
        self.message = message

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "link_id": self.link_id,
                "domain_id": self.domain_id,
                "email": self.email,
                "message": self.message,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return EmailDnsRecordRequest(
            link_id=payload.get("link_id"),
            domain_id=payload.get("domain_id"),
            email=payload.get("email"),
            message=payload.get("message"),
        )
