from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.integrations.v3.models.destination1 import Destination1
from sendgrid.rest.api.integrations.v3.models.integration_patch_filters import IntegrationPatchFilters
from sendgrid.rest.api.integrations.v3.models.integration_patch_properties import IntegrationPatchProperties



class IntegrationPatch:
    def __init__(
            self,
            destination: Optional[Destination1]=None,
            filters: Optional[IntegrationPatchFilters]=None,
            properties: Optional[IntegrationPatchProperties]=None,
            label: Optional[str]=None
    ):
        self.destination=destination
        self.filters=filters
        self.properties=properties
        self.label=label

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "destination": self.destination,
            "filters": self.filters,
            "properties": self.properties,
            "label": self.label
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return IntegrationPatch(
            destination=payload.get('destination'),
            filters=payload.get('filters'),
            properties=payload.get('properties'),
            label=payload.get('label')
        ) 

