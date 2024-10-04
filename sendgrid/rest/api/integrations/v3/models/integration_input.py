from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.integrations.v3.models.destination2 import Destination2
from sendgrid.rest.api.integrations.v3.models.integration_input_filters import (
    IntegrationInputFilters,
)
from sendgrid.rest.api.integrations.v3.models.integration_input_properties import (
    IntegrationInputProperties,
)


class IntegrationInput:
    def __init__(
        self,
        destination: Optional[Destination2] = None,
        filters: Optional[IntegrationInputFilters] = None,
        properties: Optional[IntegrationInputProperties] = None,
        label: Optional[str] = None,
    ):
        self.destination = destination
        self.filters = filters
        self.properties = properties
        self.label = label

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "destination": self.destination,
                "filters": self.filters,
                "properties": self.properties,
                "label": self.label,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return IntegrationInput(
            destination=payload.get("destination"),
            filters=payload.get("filters"),
            properties=payload.get("properties"),
            label=payload.get("label"),
        )
