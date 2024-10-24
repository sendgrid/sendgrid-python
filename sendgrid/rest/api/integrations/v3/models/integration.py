from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.integrations.v3.models.destination3 import Destination3
from sendgrid.rest.api.integrations.v3.models.integration_filters import IntegrationFilters
from sendgrid.rest.api.integrations.v3.models.integration_properties import IntegrationProperties



class Integration:
    def __init__(
            self,
            integration_id: Optional[str]=None,
            user_id: Optional[str]=None,
            filters: Optional[IntegrationFilters]=None,
            properties: Optional[IntegrationProperties]=None,
            label: Optional[str]=None,
            destination: Optional[Destination3]=None
    ):
        self.integration_id=integration_id
        self.user_id=user_id
        self.filters=filters
        self.properties=properties
        self.label=label
        self.destination=destination

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "integration_id": self.integration_id,
            "user_id": self.user_id,
            "filters": self.filters,
            "properties": self.properties,
            "label": self.label,
            "destination": self.destination
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return Integration(
            integration_id=payload.get('integration_id'),
            user_id=payload.get('user_id'),
            filters=payload.get('filters'),
            properties=payload.get('properties'),
            label=payload.get('label'),
            destination=payload.get('destination')
        ) 

