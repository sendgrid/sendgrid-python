from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class ApiKeyScopesResponse:
    def __init__(
        self,
        scopes: Optional[List[str]] = None,
        api_key_id: Optional[str] = None,
        name: Optional[str] = None,
    ):
        self.scopes = scopes
        self.api_key_id = api_key_id
        self.name = name

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "scopes": self.scopes,
                "api_key_id": self.api_key_id,
                "name": self.name,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ApiKeyScopesResponse(
            scopes=payload.get("scopes"),
            api_key_id=payload.get("api_key_id"),
            name=payload.get("name"),
        )
