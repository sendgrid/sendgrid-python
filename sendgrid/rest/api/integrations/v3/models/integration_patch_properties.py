from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.integrations.v3.models.destination_region import DestinationRegion



class IntegrationPatchProperties:
    def __init__(
            self,
            write_key: Optional[str]=None,
            destination_region: Optional[DestinationRegion]=None
    ):
        self.write_key=write_key
        self.destination_region=destination_region

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "write_key": self.write_key,
            "destination_region": self.destination_region
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return IntegrationPatchProperties(
            write_key=payload.get('write_key'),
            destination_region=payload.get('destination_region')
        ) 

