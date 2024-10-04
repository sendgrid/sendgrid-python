from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class UpdateSsoCertificateRequest:
    def __init__(
        self,
        public_certificate: Optional[str] = None,
        enabled: Optional[bool] = None,
        integration_id: Optional[str] = None,
    ):
        self.public_certificate = public_certificate
        self.enabled = enabled
        self.integration_id = integration_id

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "public_certificate": self.public_certificate,
                "enabled": self.enabled,
                "integration_id": self.integration_id,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateSsoCertificateRequest(
            public_certificate=payload.get("public_certificate"),
            enabled=payload.get("enabled"),
            integration_id=payload.get("integration_id"),
        )
