from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.integrations.v3.models.destination_region1 import (
    DestinationRegion1,
)


class IntegrationInputProperties:
    def __init__(
        self,
        write_key: Optional[str] = None,
        destination_region: Optional[DestinationRegion1] = None,
    ):
        self.write_key = write_key
        self.destination_region = destination_region

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "write_key": self.write_key,
                "destination_region": self.destination_region,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return IntegrationInputProperties(
            write_key=payload.get("write_key"),
            destination_region=payload.get("destination_region"),
        )
