from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class EventWebhookOauthResponseProps:
    def __init__(
            self,
            oauth_client_id: Optional[str]=None,
            oauth_token_url: Optional[str]=None
    ):
        self.oauth_client_id=oauth_client_id
        self.oauth_token_url=oauth_token_url

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "oauth_client_id": self.oauth_client_id,
            "oauth_token_url": self.oauth_token_url
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return EventWebhookOauthResponseProps(
            oauth_client_id=payload.get('oauth_client_id'),
            oauth_token_url=payload.get('oauth_token_url')
        ) 

