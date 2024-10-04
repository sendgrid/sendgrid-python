from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class SendTestCampaignRequest:
    def __init__(self, to: Optional[str] = None):
        self.to = to

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"to": self.to}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendTestCampaignRequest(to=payload.get("to"))
