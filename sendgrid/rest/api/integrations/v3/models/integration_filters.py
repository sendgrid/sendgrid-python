from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.integrations.v3.models.items2 import Items2


class IntegrationFilters:
    def __init__(self, email_events: Optional[List[Items2]] = None):
        self.email_events = email_events

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"email_events": self.email_events}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return IntegrationFilters(email_events=payload.get("email_events"))
