from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class SsoIntegration:
    def __init__(
        self,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        signin_url: Optional[str] = None,
        signout_url: Optional[str] = None,
        entity_id: Optional[str] = None,
        completed_integration: Optional[bool] = None,
        last_updated: Optional[float] = None,
        id: Optional[str] = None,
        single_signon_url: Optional[str] = None,
        audience_url: Optional[str] = None,
    ):
        self.name = name
        self.enabled = enabled
        self.signin_url = signin_url
        self.signout_url = signout_url
        self.entity_id = entity_id
        self.completed_integration = completed_integration
        self.last_updated = last_updated
        self.id = id
        self.single_signon_url = single_signon_url
        self.audience_url = audience_url

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "name": self.name,
                "enabled": self.enabled,
                "signin_url": self.signin_url,
                "signout_url": self.signout_url,
                "entity_id": self.entity_id,
                "completed_integration": self.completed_integration,
                "last_updated": self.last_updated,
                "id": self.id,
                "single_signon_url": self.single_signon_url,
                "audience_url": self.audience_url,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SsoIntegration(
            name=payload.get("name"),
            enabled=payload.get("enabled"),
            signin_url=payload.get("signin_url"),
            signout_url=payload.get("signout_url"),
            entity_id=payload.get("entity_id"),
            completed_integration=payload.get("completed_integration"),
            last_updated=payload.get("last_updated"),
            id=payload.get("id"),
            single_signon_url=payload.get("single_signon_url"),
            audience_url=payload.get("audience_url"),
        )
