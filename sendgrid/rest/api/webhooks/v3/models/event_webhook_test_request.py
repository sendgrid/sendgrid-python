from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class EventWebhookTestRequest:
    def __init__(
            self,
            id: Optional[str]=None,
            url: Optional[str]=None,
            oauth_client_id: Optional[str]=None,
            oauth_client_secret: Optional[str]=None,
            oauth_token_url: Optional[str]=None
    ):
        self.id=id
        self.url=url
        self.oauth_client_id=oauth_client_id
        self.oauth_client_secret=oauth_client_secret
        self.oauth_token_url=oauth_token_url

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "url": self.url,
            "oauth_client_id": self.oauth_client_id,
            "oauth_client_secret": self.oauth_client_secret,
            "oauth_token_url": self.oauth_token_url
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return EventWebhookTestRequest(
            id=payload.get('id'),
            url=payload.get('url'),
            oauth_client_id=payload.get('oauth_client_id'),
            oauth_client_secret=payload.get('oauth_client_secret'),
            oauth_token_url=payload.get('oauth_token_url')
        ) 

